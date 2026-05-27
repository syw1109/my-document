# 적용 내용
# 바이낸스 SOL/USDT 선물.
# 격리(Isolated) 마진.
# 레버리지 5배.
# 선물계좌 증거금의 50% 사용.
# 기존 SOL 포지션이 있으면 거래 안 함.

# 추세 전략 : MA18 4일 변화 추세 분석 (3일 연속 0.6% 이상 상승/하락 여부) 
# ㄴ 업비트 SOL 18일 MA가 3일 연속 0.6%이상 상승이면 숏 금지.
# ㄴ 업비트 SOL 18일 MA가 3일 연속 0.6%이상 하락이면 롱 금지.
# 지난 6일동안 같은 방향이고 변동성 0.4%이상이 5일이상 존재 상승/하락 추세로 보고 각각 숏/롱 진입 금지
# 현재가와 토요일 기준가 차이가 ±9% 이상이면 거래 금지. -> 위에 추세 전략에 해당이 되어서 빼도 되겠다.
# 업비트 기준 솔라나 시가가 어제는 43,18 위였는데, 오늘은 43,18 중 하나라도 아래면 롱 깨진 조건이니 롱 진입 금지
# 업비트 기준 솔라나 시가가 어제는 43,18 모두 위가 아니었는데, 오늘은 43,18 모두 위면 롱 진입 조건으로 숏 진입 금지
# 일,월,화,수 매일 1% TP룰
# while문으로 매일 9시에 거래 # 목요일/금요일/토요일 매매 금지.
# SOL 포지션이 있으면 금요일 종가에 close 하기, 가능하면 토요일 1시간봉 05:00봉 마감 06:00 에 close --- 보류

# 기존 상승다이버 rsi 전략
# 기존 SOL 포지션이 없어야 함.
# 직전 16개 1시간봉 중 마지막 봉을 판단봉으로 사용.
# 이전 15개 봉의 lowest low보다 직전봉 close가 더 낮아야 함.
# 이전 15개 봉의 lowest rsi보다 직전봉 rsi가 2% 이상 높아야 함.
# 직전봉의 open 대비 close 변동폭이 0.3% 이상이어야 함.
# 진입 후 직전 캔들 종가값 대비 롱인 경우는+1% 값에,  T.P (take profit)걸기
# 진입 비중은 계좌 달러의 0.5배로 시장가로 들어가고 진입 레버리지는 5배.


# 1. 하락 다이버전스일때 숏 진입하는 조건을 추가해주세요.
# 직전 16개 1시간봉 중 마지막 봉을 판단봉으로 사용.
# 이전 15개 봉의 highest high보다 직전봉 close가 더 높아야 함.
# 이전 15개 봉의 highest rsi보다 직전봉 rsi가 2% 이상 낮아야 함.
# 직전봉의 open 대비 close 변동폭이 0.3% 이상이어야 함.
# 진입 후 직전 캔들 종가값 대비 롱인 경우는+1% 값에, 숏인 경우는 -1% 값에 T.P (take profit)걸기
# 진입 비중은 계좌 달러의 0.5배로 시장가로 들어가고 진입 레버리지는 5배

# 2. 1hr봉 전략과 동일하게 15m봉 전략도 똑같이 만들어주세요.
# 즉 1hr봉도 보고 15m분 봉으로도 모니터링 하다가 1hr 봉 기준에 만족 안되면 15m 봉을 보는 식으로 해주시면 되겠습니다. 
# 직전 16개봉 15분봉 중 마지막봉을 판단봉 사용.
# 하락 다이버전스일때는 숏, 상승 다이버전스 일때는 롱으로 진입 합니다
# 진입 후 직전 캔들 종가값 대비 롱인 경우는+0.9% 값에, 숏인 경우는 -0.9% 값에 T.P (take profit)걸기
# 진입 비중은 계좌 달러의 0.5배로 시장가로 들어가고 진입 레버리지는 5배

# 3. btc 비트코인도 rsi 룰을 추가해주세요.
# 1hr봉 기준, 15분봉 기준
# 상승 다이버전스, 하락 다이버전스
# btc는변동성이 작으니 1시간봉, 15분봉 모두 T.P값을 0.5% 값으로 해주세요. 
# 30분봉도 추가
# cme값과 1%이상 차이 날때만 포지션 진입.

# + 추가하려는 전략
# 다이버 전략에도 3일,6일 추세 값과, 이평선 깨지거나 돌파시에 롱 숏 진입 금지룰 동일하게 적용하고 싶음


# 바이낸스 선물 거래소 연결
exchange = ccxt.binance({
    'apiKey': 'QAK7GNH9rWZTCTaozqdNJOR9zsxB6N8QJieYRMDvXDt27ngVEwJs9tDOMAQsc1Bi',
    'secret': 'i8nNaQnZnsDL8gpAK7Q8yAWpxHZH9RYuHTY1q7ohMw9j1NXnmc1T6VCwetjfO48P',
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future',
    },
})



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
UPBIT_TICKER = 'KRW-SOL'
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


#바이낸스용 rsi 계산식
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


def trade_rsi_strategy(symbol, market_id, timeframe, tp_long_pct, tp_short_pct, min_volatility=0.003, use_position_check=True):
    """공통 RSI 전략 실행 함수"""
    set_margin_and_leverage(symbol)

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

    # CME 편차 조건: Bull 이나 Bear 신호가 있을 때만 확인
    if (bull and bull["signal"]) or (bear and bear["signal"]):
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

    if bull and bull["signal"]:
        tp_price = bull["prev_close"] * (1 + tp_long_pct)
        exchange.create_market_buy_order(symbol, amount)
        place_tp_long(symbol, amount, tp_price)
        print(f"[{symbol} {timeframe}] 롱 진입 | amount={amount} | price={current_price} | tp={tp_price}")
        return

    if bear and bear["signal"]:
        tp_price = bear["prev_close"] * (1 - tp_short_pct)
        exchange.create_market_sell_order(symbol, amount)
        place_tp_short(symbol, amount, tp_price)
        print(f"[{symbol} {timeframe}] 숏 진입 | amount={amount} | price={current_price} | tp={tp_price}")
        return

    print(f"[{symbol} {timeframe}] 진입 조건 없음")



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


def get_upbit_ma18_ma43():
    """업비트 일봉 기준 MA18, MA43을 계산해 최근 확정봉 기준 값 반환"""
    df = pyupbit.get_ohlcv(UPBIT_TICKER, interval="day", count=60)
    if df is None or len(df) < 44:
        raise ValueError("업비트 일봉 데이터가 부족합니다.")

    df["ma18"] = df["close"].rolling(18).mean()
    df["ma43"] = df["close"].rolling(43).mean()

    prev = df.dropna().iloc[-2]
    return float(prev["ma18"]), float(prev["ma43"])


def get_upbit_yesterday_ma18_ma43():
    """어제 기준 MA18, MA43을 조회"""
    df = pyupbit.get_ohlcv(UPBIT_TICKER, interval="day", count=61)
    if df is None or len(df) < 45:
        raise ValueError("업비트 어제 MA 데이터 부족")

    df["ma18"] = df["close"].rolling(18).mean()
    df["ma43"] = df["close"].rolling(43).mean()

    yesterday = df.dropna().iloc[-2]
    return float(yesterday["ma18"]), float(yesterday["ma43"])


def get_upbit_today_open():
    """오늘 업비트 SOL 시가 조회"""
    df = pyupbit.get_ohlcv(UPBIT_TICKER, interval="day", count=3)
    if df is None or len(df) < 2:
        raise ValueError("업비트 오픈가 데이터를 가져오지 못했습니다.")
    return float(df.iloc[-1]["open"])


def get_upbit_yesterday_open():
    """어제 업비트 SOL 시가 조회"""
    df = pyupbit.get_ohlcv(UPBIT_TICKER, interval="day", count=3)
    if df is None or len(df) < 2:
        raise ValueError("업비트 어제 시가 데이터 부족")
    return float(df.iloc[-2]["open"])


def get_upbit_ma18_series():
    """업비트 일봉 MA18 시리즈를 반환"""
    df = pyupbit.get_ohlcv(UPBIT_TICKER, interval="day", count=30)
    if df is None or len(df) < 18:
        raise ValueError("업비트 일봉 데이터가 부족합니다.")
    df["ma18"] = df["close"].rolling(18).mean()
    return df["ma18"].dropna()


def ma18_4day_change_trend():
    """최근 4일 MA18 변화율을 보고 3일 연속 상승/하락 여부를 판단"""
    ma = get_upbit_ma18_series()
    last5 = ma.iloc[-5:].tolist()
    if len(last5) < 5:
        return None

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


def ma18_6day_volatility_trend():
    """지난 6일 MA18이 같은 방향으로 움직이고 변동성이 큰 날이 많은지 분석"""
    ma = get_upbit_ma18_series()
    if len(ma) < 7:
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


# ===================== 메인 루프 수정: 15 분봉과 1 시간봉 독립 실행 =====================
      
import threading

last_run_date = None
last_1h_run_mark = None
last_15m_run_mark = None
run_lock = threading.Lock()  # 동시에 같은 심볼 중복 실행 방지

def run_1h_strategies():
    try:
        if not has_position(MARKET_ID_SOL):
            trade_rsi_strategy(SOL_SYMBOL, MARKET_ID_SOL, '1h', 0.01, 0.01, 0.003)
        if not has_position(MARKET_ID_BTC):
            trade_rsi_strategy(BTC_SYMBOL, MARKET_ID_BTC, '1h', 0.005, 0.005, 0.003)
    except Exception as e:
        print(f"[1h thread error] {e}")

def run_15m_strategies():
    try:
        if not has_position(MARKET_ID_SOL):
            trade_rsi_strategy(SOL_SYMBOL, MARKET_ID_SOL, '15m', 0.009, 0.009, 0.0025)
        if not has_position(MARKET_ID_BTC):
            trade_rsi_strategy(BTC_SYMBOL, MARKET_ID_BTC, '15m', 0.005, 0.005, 0.0024)
    except Exception as e:
        print(f"[15m thread error] {e}")

while True:
    try:
        now = now_kst()

        # 09:00 SOL 전략
        if now.hour == 9 and now.minute == 0:
            if last_run_date != now.date():
                last_run_date = now.date()  # ← 먼저 세팅해서 중복 방지
                threading.Thread(target=trade_once_sol, daemon=True).start()

        # 1시간봉: 매 정각
        if now.minute == 0:
            current_1h_mark = now.replace(minute=0, second=0, microsecond=0)
            if last_1h_run_mark != current_1h_mark:
                last_1h_run_mark = current_1h_mark  # ← 먼저 세팅
                threading.Thread(target=run_1h_strategies, daemon=True).start()

        # 15분봉: 15, 30, 45분 (00분은 위에서 처리)
        if now.minute % 15 == 0:
            current_15m_mark = now.replace(
                minute=(now.minute // 15) * 15, second=0, microsecond=0
            )
            if last_15m_run_mark != current_15m_mark:
                last_15m_run_mark = current_15m_mark  # ← 먼저 세팅
                threading.Thread(target=run_15m_strategies, daemon=True).start()

        time.sleep(1)

    except Exception as e:
        print(e)
        time.sleep(2)      