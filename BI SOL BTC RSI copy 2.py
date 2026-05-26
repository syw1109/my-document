
# ma18 3일 변동성, 6일 변동성에 따른 다이버전스 진입 제한룰 추가
# ma18_4day_change_trend
# 최근 4일 MA18 변화율을 보고 3일 연속 상승/하락 여부를 판단하여 상승장에는 숏 금지, 하락장에는 롱금지
# ma18_6day_volatility_trend
# 지난 6일 MA18이 같은 방향으로 움직이고 변동성이 큰 날이 많은지 분석하여 상승장에는 숏 금지, 하락장에는 롱금지
#  MA18 은 SOL 기준과 BTC 기준 분리

import time
import datetime
import ccxt
import pyupbit
import pandas as pd
import numpy as np
from datetime import timezone, timedelta


# ===================== 기본 설정 =====================

# KST 타임존 설정 및 전역 변수
KST = timezone(timedelta(hours=9))
SOL_SYMBOL = 'SOL/USDT'
BTC_SYMBOL = 'BTC/USDT'
UPBIT_TICKER_SOL = 'KRW-SOL'
UPBIT_TICKER_BTC = 'KRW-BTC'
MARKET_ID_SOL = 'SOLUSDT'
MARKET_ID_BTC = 'BTCUSDT'
LEVERAGE = 5


# 바이낸스 선물 거래소 연결
exchange = ccxt.binance({
    'apiKey': '',
    'secret': '',
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future',
    },
})


print("autotrade start")


def now_kst():
    """현재 KST 시간을 반환"""
    return datetime.datetime.now(KST)


now = now_kst()
print(now)


# ===================== 공통 유틸 =====================


def get_available_usdt():
    """선물 계좌의 사용 가능 USDT 잔고를 반환"""
    balance = exchange.fetch_balance(params={'type': 'future'})
    return float(balance.get('free', {}).get('USDT', 0))


def set_margin_and_leverage(symbol):
    """지정 심볼을 isolated 마진으로 설정하고 레버리지를 적용"""
    exchange.load_markets()
    exchange.set_margin_mode('isolated', symbol)
    exchange.set_leverage(LEVERAGE, symbol)


def place_tp_long(symbol, qty, tp_price):
    """롱 포지션용 TAKE_PROFIT_MARKET 주문 생성"""
    exchange.create_order(
        symbol=symbol,
        type='TAKE_PROFIT_MARKET',
        side='sell',
        amount=qty,
        params={
            'stopPrice': tp_price,
            'closePosition': True,
            'workingType': 'MARK_PRICE'
        }
    )


def place_tp_short(symbol, qty, tp_price):
    """숏 포지션용 TAKE_PROFIT_MARKET 주문 생성"""
    exchange.create_order(
        symbol=symbol,
        type='TAKE_PROFIT_MARKET',
        side='buy',
        amount=qty,
        params={
            'stopPrice': tp_price,
            'closePosition': True,
            'workingType': 'MARK_PRICE'
        }
    )


def has_position(symbol_market_id):
    """지정한 심볼의 포지션 보유 여부 확인"""
    balance = exchange.fetch_balance(params={'type': 'future'})
    positions = balance.get('info', {}).get('positions', [])
    for p in positions:
        if p.get('symbol') == symbol_market_id and abs(float(p.get('positionAmt', 0))) > 0:
            return True
    return False


# ===================== RSI 계산 =====================


def get_rsi_dataframe(symbol, timeframe='1h', limit=200, rsi_length=14, debug=False):
    """Wilder 방식(RMA)으로 RSI를 계산"""
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    if ohlcv is None or len(ohlcv) < rsi_length + 16:
        raise ValueError(f"{symbol} {timeframe} 데이터가 부족합니다.")

    df = pd.DataFrame(ohlcv, columns=['ts', 'open', 'high', 'low', 'close', 'volume'])

    delta = df['close'].diff()
    gain = delta.clip(lower=0)
    loss = (-delta).clip(lower=0)

    avg_gain = pd.Series(index=df.index, dtype='float64')
    avg_loss = pd.Series(index=df.index, dtype='float64')

    avg_gain.iloc[rsi_length] = gain.iloc[1:rsi_length+1].mean()
    avg_loss.iloc[rsi_length] = loss.iloc[1:rsi_length+1].mean()

    for i in range(rsi_length + 1, len(df)):
        avg_gain.iloc[i] = (avg_gain.iloc[i - 1] * (rsi_length - 1) + gain.iloc[i]) / rsi_length
        avg_loss.iloc[i] = (avg_loss.iloc[i - 1] * (rsi_length - 1) + loss.iloc[i]) / rsi_length

    rs = avg_gain / avg_loss.replace(0, np.nan)
    df['rsi'] = 100 - (100 / (1 + rs))

    if debug:
        last_row = df.iloc[-1]
        prev_row = df.iloc[-2]
        print(f"[RSI DEBUG] {symbol} {timeframe}")
        print(f"[RSI DEBUG] last_close={last_row['close']:.6f}, last_rsi={last_row['rsi']:.4f}")
        print(f"[RSI DEBUG] prev_close={prev_row['close']:.6f}, prev_rsi={prev_row['rsi']:.4f}")
        print(f"[RSI DEBUG] recent_rsi_tail={df['rsi'].tail(5).round(4).tolist()}")

    return df


# ===================== RSI 다이버전스 판단 =====================


def analyze_bullish_divergence(symbol, timeframe, base_count=15, rsi_raise_pct=0.02, min_volatility=0.003):
    """
    상승 다이버전스 조건 판단:
    - 직전 16개 봉 중 마지막 봉을 판단봉으로 사용
    - 이전 15개 봉의 lowest low보다 직전봉 close가 더 낮아야 함
    - 이전 15개 봉의 lowest rsi보다 직전봉 rsi가 지정 비율 이상 높아야 함
    - 직전봉 open 대비 close 변동폭이 최소 기준 이상이어야 함
    """
    df = get_rsi_dataframe(symbol, timeframe=timeframe)

    # 현재 진행 중인 봉 제외하고 직전 16개 완성봉만 사용
    recent = df.iloc[-17:-1].copy()
    recent = recent.dropna(subset=['rsi'])

    if len(recent) < 16:
        return None

    prev_candle = recent.iloc[-1]     # 직전 마감봉
    base_15 = recent.iloc[:-1].copy() # 그 이전 15개 봉

    lowest_low = base_15['low'].min()
    lowest_rsi = base_15['rsi'].min()

    cond_price = prev_candle['close'] < lowest_low
    cond_rsi = prev_candle['rsi'] >= lowest_rsi * (1 + rsi_raise_pct)
    cond_volatility = abs(prev_candle['close'] - prev_candle['open']) / prev_candle['open'] >= min_volatility

    signal = cond_price and cond_rsi and cond_volatility

    return {
        "signal": signal,
        "side": "long",
        "lowest_low": float(lowest_low),
        "lowest_rsi": float(lowest_rsi),
        "prev_open": float(prev_candle['open']),
        "prev_close": float(prev_candle['close']),
        "prev_rsi": float(prev_candle['rsi']),
        "price_condition": cond_price,
        "rsi_condition": cond_rsi,
        "volatility_condition": cond_volatility,
        "tp_price": float(prev_candle['close'])
    }


def analyze_bearish_divergence(symbol, timeframe, base_count=15, rsi_drop_pct=0.02, min_volatility=0.003):
    """
    하락 다이버전스 조건 판단:
    - 직전 16개 봉 중 마지막 봉을 판단봉으로 사용
    - 이전 15개 봉의 highest high보다 직전봉 close가 더 높아야 함
    - 이전 15개 봉의 highest rsi보다 직전봉 rsi가 지정 비율 이상 낮아야 함
    - 직전봉 open 대비 close 변동폭이 최소 기준 이상이어야 함
    """
    df = get_rsi_dataframe(symbol, timeframe=timeframe)

    # 현재 진행 중인 봉 제외하고 직전 16개 완성봉만 사용
    recent = df.iloc[-17:-1].copy()
    recent = recent.dropna(subset=['rsi'])

    if len(recent) < 16:
        return None

    prev_candle = recent.iloc[-1]
    base_15 = recent.iloc[:-1].copy()

    highest_high = base_15['high'].max()
    highest_rsi = base_15['rsi'].max()

    cond_price = prev_candle['close'] > highest_high
    cond_rsi = prev_candle['rsi'] <= highest_rsi * (1 - rsi_drop_pct)
    cond_volatility = abs(prev_candle['close'] - prev_candle['open']) / prev_candle['open'] >= min_volatility

    signal = cond_price and cond_rsi and cond_volatility

    return {
        "signal": signal,
        "side": "short",
        "highest_high": float(highest_high),
        "highest_rsi": float(highest_rsi),
        "prev_open": float(prev_candle['open']),
        "prev_close": float(prev_candle['close']),
        "prev_rsi": float(prev_candle['rsi']),
        "price_condition": cond_price,
        "rsi_condition": cond_rsi,
        "volatility_condition": cond_volatility,
        "tp_price": float(prev_candle['close'])
    }


# ===================== MA18 공통 유틸 (SOL/BTC 별로 분리 가능) =====================

def get_ma18_series(ticker, count=30, window=18):
    """
    업비트 일봉 기준 특정 티커(예: KRW-SOL, KRW-BTC)의 MA18 시리즈를 반환
    """
    df = pyupbit.get_ohlcv(ticker, interval="day", count=count)
    if df is None or len(df) < window:
        return None
    df["ma18"] = df["close"].rolling(window).mean()
    return df["ma18"].dropna()


def get_ma18_4day_change_trend(ticker):
    """
    특정 티커(예: KRW-SOL, KRW-BTC) 기준 MA18 4일 변화율 + 3일 연속 상승/하락 판단
    """
    ma = get_ma18_series(ticker, count=30, window=18)
    if ma is None or len(ma) < 5:
        return None

    last5 = ma.iloc[-5:].tolist()
    changes = []

    for i in range(1, 5):
        prev = last5[i - 1]
        cur = last5[i]
        change_pct = (cur / prev - 1) * 100
        changes.append(change_pct)

    up_3days = changes[0] >= 0.6 and changes[1] >= 0.6 and changes[2] >= 0.6
    down_3days = changes[0] <= -0.6 and changes[1] <= -0.6 and changes[2] <= -0.6

    return {
        "up_3days": up_3days,
        "down_3days": down_3days,
        "changes": changes,
        "last_ma18": last5[-1]
    }


def get_ma18_6day_volatility_trend(ticker):
    """
    특정 티커 기준 MA18 6일 변화 + 변동성 날짜 수 계산
    """
    ma = get_ma18_series(ticker, count=30, window=18)
    if ma is None or len(ma) < 7:
        return None

    last7 = ma.iloc[-7:].tolist()
    changes = []

    for i in range(1, 7):
        prev = last7[i - 1]
        cur = last7[i]
        change_pct = (cur / prev - 1) * 100
        changes.append(change_pct)

    all_up = all(c > 0 for c in changes)
    all_down = all(c < 0 for c in changes)
    high_vol_days = sum(abs(c) >= 0.4 for c in changes)

    return {
        "all_up_6days": all_up,
        "all_down_6days": all_down,
        "high_vol_days": high_vol_days,
        "changes": changes,
        "last_ma18": last7[-1]
    }


def get_ma18_market_bias_for_symb(symbol, ticker):
    """
    특정 심볼에 대해(예: SOL/USDT) 해당 업비트 티커 기준으로
    상승/하락장 판단을 반환 (MA18 4일 + 6일 기준)
    """
    trend4 = get_ma18_4day_change_trend(ticker)
    trend6 = get_ma18_6day_volatility_trend(ticker)

    if trend4 is None or trend6 is None:
        return None

    bullish_market = trend4["up_3days"] or trend6["all_up_6days"]
    bearish_market = trend4["down_3days"] or trend6["all_down_6days"]

    return {
        "ticker": ticker,
        "trend4": trend4,
        "trend6": trend6,
        "bullish_market": bullish_market,
        "bearish_market": bearish_market
    }


# ===================== 공통 RSI 전략 실행 함수 (SOL/BTC 별 MA18 필터 적용) =====================

def trade_rsi_strategy(symbol, market_id, timeframe, tp_long_pct, tp_short_pct, min_volatility=0.003, use_position_check=True):
    """공통 RSI 전략 실행 함수"""
    set_margin_and_leverage(symbol)

    # 심볼별 업비트 티커 매핑
    if symbol == SOL_SYMBOL:
        upbit_ticker = UPBIT_TICKER_SOL
    elif symbol == BTC_SYMBOL:
        upbit_ticker = UPBIT_TICKER_BTC
    else:
        print(f"[{symbol} {timeframe}] 지원하지 않는 심볼")
        return

    # 심볼별 포지션이 있으면 추가 진입 금지
    if use_position_check and has_position(market_id):
        print(f"[{symbol} {timeframe}] 기존 포지션이 있어서 거래하지 않음")
        return

    available_usdt = get_available_usdt()

    # 선물 계좌 잔고의 50%를 증거금으로 사용
    margin_to_use = available_usdt * 0.5
    current_price = float(exchange.fetch_ticker(symbol)['last'])
    notional = margin_to_use * LEVERAGE
    amount = round(notional / current_price, 3)

    if amount <= 0:
        print(f"[{symbol} {timeframe}] 주문 수량이 0이라서 중단")
        return

    # RSI 다이버전스 신호 계산
    bull = analyze_bullish_divergence(
        symbol=symbol,
        timeframe=timeframe,
        base_count=15,
        rsi_raise_pct=0.02,
        min_volatility=min_volatility
    )

    bear = analyze_bearish_divergence(
        symbol=symbol,
        timeframe=timeframe,
        base_count=15,
        rsi_drop_pct=0.02,
        min_volatility=min_volatility
    )

    print(f"[{symbol} {timeframe}] BULL={bull}")
    print(f"[{symbol} {timeframe}] BEAR={bear}")

    # 해당 심볼에 맞는 MA18 기반 추세 필터 가져오기 (SOL/BTC 각각 별도)
    bias = get_ma18_market_bias_for_symb(symbol, upbit_ticker)
    if bias is None:
        print(f"[{symbol} {timeframe}] MA18 추세 필터 데이터를 가져오지 못해 진입 중단")
        return

    bullish_market = bias["bullish_market"]
    bearish_market = bias["bearish_market"]

    print(f"[{symbol} {timeframe}] MA18 bias({upbit_ticker}): bullish={bullish_market}, bearish={bearish_market}")

    # CME 편차 조건: Bull 이나 Bear 신호가 있을 때만 확인
    if bull and bull["signal"] or bear and bear["signal"]:
        try:
            cme_price = get_last_saturday_6_close()
        except Exception as e:
            print(f"[{symbol} {timeframe}] 토요일 06:00 가격 조회 실패: {e}")
            return

        prev_close = bull["prev_close"] if bull and bull["signal"] else bear["prev_close"]
        deviation = abs(prev_close - cme_price) / cme_price

        if deviation < 0.01:  # 1% 미만
            print(f"[{symbol} {timeframe}] CME 편차 {deviation*100:.2f}% 미만으로 진입 금지 | CME={cme_price:.2f}, prev_close={prev_close:.2f}")
            return

        print(f"[{symbol} {timeframe}] CME 편차 {deviation*100:.2f}% 충족 | CME={cme_price:.2f}, prev_close={prev_close:.2f}")

    # 롱 진입 (하락장이면 금지)
    if bull and bull["signal"]:
        if bearish_market:
            print(f"[{symbol} {timeframe}] 하락장 필터로 롱 진입 금지")
            return

        tp_price = bull["prev_close"] * (1 + tp_long_pct)
        exchange.create_market_buy_order(symbol, amount)
        place_tp_long(symbol, amount, tp_price)
        print(f"[{symbol} {timeframe}] 롱 진입 | amount={amount} | price={current_price} | tp={tp_price}")
        return

    # 숏 진입 (상승장이면 금지)
    if bear and bear["signal"]:
        if bullish_market:
            print(f"[{symbol} {timeframe}] 상승장 필터로 숏 진입 금지")
            return

        tp_price = bear["prev_close"] * (1 - tp_short_pct)
        exchange.create_market_sell_order(symbol, amount)
        place_tp_short(symbol, amount, tp_price)
        print(f"[{symbol} {timeframe}] 숏 진입 | amount={amount} | price={current_price} | tp={tp_price}")
        return

    print(f"[{symbol} {timeframe}] 진입 조건 없음")


# ===================== 봉 실행 시간 체크 (15분, 30분, 1시간) =====================

# 봉 놓치는 것 방지
def is_15m_execution_time(now):
    return now.minute % 15 == 0 and now.second < 15


def is_30m_execution_time(now):
    """30 분봉: 분 %30 == 0 이고 초 < 15 일 때만 실행"""
    return now.minute % 30 == 0 and now.second < 15


def is_1h_execution_time(now):
    return now.minute == 0 and now.second < 15


# ===================== 09:00 SOL 기존 전략 =====================


def get_last_saturday_6_close():
    """가장 최근 토요일 06:00의 1시간봉 종가를 조회"""
    now = now_kst()
    sat6 = now.replace(hour=6, minute=0, second=0, microsecond=0)

    while sat6.weekday() != 5:
        sat6 -= datetime.timedelta(days=1)

    if now < sat6:
        sat6 -= datetime.timedelta(days=7)

    since_ms = int((sat6 - datetime.timedelta(days=7)).timestamp() * 1000)
    klines = exchange.fetch_ohlcv(SOL_SYMBOL, timeframe='1h', since=since_ms, limit=200)
    target_ms = int(sat6.astimezone(datetime.timezone.utc).timestamp() * 1000)

    for o in klines:
        if o[0] == target_ms:
            return float(o[4])

    raise ValueError("토요일 06:00 종가를 찾지 못했습니다.")


# SOL 09:00 전략용 MA18 관련 함수는 기존 코드 유지 (SOL용만 사용)
def get_upbit_ma18_ma43():
    """업비트 일봉 기준 MA18, MA43을 계산해 최근 확정봉 기준 값 반환"""
    df = pyupbit.get_ohlcv(UPBIT_TICKER_SOL, interval="day", count=60)
    if df is None or len(df) < 44:
        raise ValueError("업비트 일봉 데이터가 부족합니다.")

    df["ma18"] = df["close"].rolling(18).mean()
    df["ma43"] = df["close"].rolling(43).mean()

    prev = df.dropna().iloc[-2]
    return float(prev["ma18"]), float(prev["ma43"])


def get_upbit_yesterday_ma18_ma43():
    """어제 기준 MA18, MA43을 조회"""
    df = pyupbit.get_ohlcv(UPBIT_TICKER_SOL, interval="day", count=61)
    if df is None or len(df) < 45:
        raise ValueError("업비트 어제 MA 데이터 부족")

    df["ma18"] = df["close"].rolling(18).mean()
    df["ma43"] = df["close"].rolling(43).mean()

    yesterday = df.dropna().iloc[-2]
    return float(yesterday["ma18"]), float(yesterday["ma43"])


def get_upbit_today_open():
    """오늘 업비트 SOL 시가 조회"""
    df = pyupbit.get_ohlcv(UPBIT_TICKER_SOL, interval="day", count=3)
    if df is None or len(df) < 2:
        raise ValueError("업비트 오픈가 데이터를 가져오지 못했습니다.")
    return float(df.iloc[-1]["open"])


def get_upbit_yesterday_open():
    """어제 업비트 SOL 시가 조회"""
    df = pyupbit.get_ohlcv(UPBIT_TICKER_SOL, interval="day", count=3)
    if df is None or len(df) < 2:
        raise ValueError("업비트 어제 시가 데이터 부족")
    return float(df.iloc[-2]["open"])


def get_upbit_ma18_series():
    """업비트 일봉 MA18 시리즈를 반환 (SOL 전용)"""
    df = pyupbit.get_ohlcv(UPBIT_TICKER_SOL, interval="day", count=30)
    if df is None or len(df) < 18:
        raise ValueError("업비트 일봉 데이터가 부족합니다.")
    df["ma18"] = df["close"].rolling(18).mean()
    return df["ma18"].dropna()


def ma18_4day_change_trend():
    """SOL 전용 09:00 전략을 위한 MA18 4일 변화율 판단 (상위 전략용)"""
    return get_ma18_4day_change_trend(UPBIT_TICKER_SOL)


def ma18_6day_volatility_trend():
    """SOL 전용 09:00 전략을 위한 MA18 6일 변동성 판단 (상위 전략용)"""
    return get_ma18_6day_volatility_trend(UPBIT_TICKER_SOL)


def trade_once_sol():
    """매일 09:00에 실행하는 기존 SOL 전략"""
    set_margin_and_leverage(SOL_SYMBOL)

    now = now_kst()
    if now.weekday() in [3, 4, 5]:
        print("목요일/금요일/토요일은 매매 금지")
        return

    if has_position(MARKET_ID_SOL):
        print("기존 SOL 포지션이 있어서 거래하지 않음")
        return

    sat_close = get_last_saturday_6_close()
    current_price = float(exchange.fetch_ticker(SOL_SYMBOL)['last'])

    trend = ma18_4day_change_trend()
    if trend is None:
        print("MA18 추세 데이터를 가져오지 못했습니다.")
        return

    vol_trend = ma18_6day_volatility_trend()
    if vol_trend is None:
        print("MA18 6일 변동성 추세 데이터를 가져오지 못했습니다.")
        return

    upbit_ma18, upbit_ma43 = get_upbit_ma18_ma43()
    yesterday_ma18, yesterday_ma43 = get_upbit_yesterday_ma18_ma43()
    upbit_today_open = get_upbit_today_open()
    upbit_yesterday_open = get_upbit_yesterday_open()

    yesterday_above_both = (upbit_yesterday_open > yesterday_ma18 and upbit_yesterday_open > yesterday_ma43)
    today_below_either = (upbit_today_open < upbit_ma18 or upbit_today_open < upbit_ma43)

    yesterday_not_above_both = (upbit_yesterday_open <= yesterday_ma18 or upbit_yesterday_open <= yesterday_ma43)
    today_above_both = (upbit_today_open > upbit_ma18 and upbit_today_open > upbit_ma43)

    available_usdt = get_available_usdt()
    margin_to_use = available_usdt * 0.5
    notional = margin_to_use * LEVERAGE
    amount = round(notional / current_price, 3)

    if amount <= 0:
        print("주문 수량이 0이라서 중단")
        return

    tp_price_long = current_price * 1.0105
    tp_price_short = current_price * 0.99

    print(f"[INFO] sat_close={sat_close}, current_price={current_price}")
    print(f"[UPBIT] today_open={upbit_today_open}, ma18={upbit_ma18}, ma43={upbit_ma43}")
    print(f"[YEST] yest_open={upbit_yesterday_open}, y_ma18={yesterday_ma18}, y_ma43={yesterday_ma43}")
    print(f"[TREND4] changes={trend['changes']}, up_3days={trend['up_3days']}, down_3days={trend['down_3days']}")
    print(f"[TREND6] all_up_6days={vol_trend['all_up_6days']}, all_down_6days={vol_trend['all_down_6days']}, high_vol_days={vol_trend['high_vol_days']}")
    print(now)

    if current_price <= sat_close * 0.99:
        if trend["down_3days"]:
            print("3일 연속 0.6% 이상 하락이라 롱 진입 금지")
            return

        if vol_trend["all_down_6days"] and vol_trend["high_vol_days"] >= 5:
            print("6일 연속 하락 + 변동성 0.4%이상 5일이상 → 롱 진입 금지")
            return

        if yesterday_above_both and today_below_either:
            print("어제 MA위→오늘 MA아래 전환으로 롱 진입 금지")
            return

        exchange.create_market_buy_order(SOL_SYMBOL, amount)
        place_tp_long(SOL_SYMBOL, amount, tp_price_long)
        print(f"롱 진입 | amount={amount} | price={current_price} | tp={tp_price_long}")
        return

    elif current_price >= sat_close * 1.01:
        if trend["up_3days"]:
            print("3일 연속 0.6% 이상 상승이라 숏 진입 금지")
            return

        if vol_trend["all_up_6days"] and vol_trend["high_vol_days"] >= 5:
            print("6일 연속 상승 + 변동성 0.4%이상 5일이상 → 숏 진입 금지")
            return

        if yesterday_not_above_both and today_above_both:
            print("어제 MA아래→오늘 MA위 전환으로 숏 진입 금지")
            return

        exchange.create_market_sell_order(SOL_SYMBOL, amount)
        place_tp_short(SOL_SYMBOL, amount, tp_price_short)
        print(f"숏 진입 | amount={amount} | price={current_price} | tp={tp_price_short}")
        return

    else:
        print("진입 조건 없음")


# ===================== 메인 루프 (1시간, 30분, 15분 버전 모두 SOL/BTC별 MA18 필터 적용) =====================

last_run_date = None
last_1h_run_mark = None
last_30m_run_mark = None
last_15m_run_mark = None

while True:
    try:
        now = now_kst()

        # 09:00 KST 에 기존 SOL 전략 실행
        if now.hour == 9 and now.minute == 0 and now.second < 10:
            if last_run_date != now.date():
                if not has_position(MARKET_ID_SOL):
                    trade_once_sol()
                last_run_date = now.date()

        # 1 시간봉 RSI 전략: 매 정각 실행 (15 분봉보다 먼저)
        if is_1h_execution_time(now):
            current_1h_mark = now.replace(minute=0, second=0, microsecond=0)
            if last_1h_run_mark != current_1h_mark:
                # SOL 1 시간봉 전략
                if not has_position(MARKET_ID_SOL):
                    trade_rsi_strategy(
                        symbol=SOL_SYMBOL,
                        market_id=MARKET_ID_SOL,
                        timeframe='1h',
                        tp_long_pct=0.01,
                        tp_short_pct=0.01,
                        min_volatility=0.003,
                        use_position_check=True
                    )

                # BTC 1 시간봉 전략
                if not has_position(MARKET_ID_BTC):
                    trade_rsi_strategy(
                        symbol=BTC_SYMBOL,
                        market_id=MARKET_ID_BTC,
                        timeframe='1h',
                        tp_long_pct=0.005,
                        tp_short_pct=0.005,
                        min_volatility=0.003,
                        use_position_check=True
                    )

                last_1h_run_mark = current_1h_mark

        # 30 분봉 RSI 전략: 00, 30 분마다 실행 (1 시간봉 이후)
        if is_30m_execution_time(now):
            current_30m_mark = now.replace(minute=(now.minute // 30) * 30, second=0, microsecond=0)
            if last_30m_run_mark != current_30m_mark:
                # SOL 30 분봉 전략
                if not has_position(MARKET_ID_SOL):
                    trade_rsi_strategy(
                        symbol=SOL_SYMBOL,
                        market_id=MARKET_ID_SOL,
                        timeframe='30m',
                        tp_long_pct=0.01,
                        tp_short_pct=0.01,
                        min_volatility=0.003,
                        use_position_check=True
                    )

                # BTC 30 분봉 전략
                if not has_position(MARKET_ID_BTC):
                    trade_rsi_strategy(
                        symbol=BTC_SYMBOL,
                        market_id=MARKET_ID_BTC,
                        timeframe='30m',
                        tp_long_pct=0.005,
                        tp_short_pct=0.005,
                        min_volatility=0.003,
                        use_position_check=True
                    )

                last_30m_run_mark = current_30m_mark

        # 15 분봉 RSI 전략: 00, 15, 30, 45 분마다 실행 (1 시간봉 이후)
        if is_15m_execution_time(now):
            current_15m_mark = now.replace(minute=(now.minute // 15) * 15, second=0, microsecond=0)
            if last_15m_run_mark != current_15m_mark:
                # SOL 15 분봉 전략
                if not has_position(MARKET_ID_SOL):
                    trade_rsi_strategy(
                        symbol=SOL_SYMBOL,
                        market_id=MARKET_ID_SOL,
                        timeframe='15m',
                        tp_long_pct=0.009,
                        tp_short_pct=0.009,
                        min_volatility=0.0025,
                        use_position_check=True
                    )

                # BTC 15 분봉 전략
                if not has_position(MARKET_ID_BTC):
                    trade_rsi_strategy(
                        symbol=BTC_SYMBOL,
                        market_id=MARKET_ID_BTC,
                        timeframe='15m',
                        tp_long_pct=0.005,
                        tp_short_pct=0.005,
                        min_volatility=0.0024,
                        use_position_check=True
                    )

                last_15m_run_mark = current_15m_mark

        time.sleep(1)

    except Exception as e:
        print(e)
        time.sleep(2)