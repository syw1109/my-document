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
# 다이버 전략에도 3일,6일 추세 값과, 이평선 깨지거나 돌파시에 롱 숏 진입 금지룰 동일하게 적용하고 싶음
# lowest close 기준 전략도 추가

# 26/6/4
# 0. 다이버 전략에도 업비트 솔라나 ma18,43룰 진입기준 바뀌는때에 롱숏 금지룰 추가 - o
# 1. 09:00 룰 Cme 1% 룰 추가필요 - o
# 2.lowest close, highest close 기준 롱숏 룰 추가, 0.3% 올랐 을때만 진입 룰 -o
# 3.btc빼기-물타기를 두배로해서 자원고갈 - 위험  - o
# 4.xrp 추가 롱 매수룰(하락추세룰, ma18,43 진입룰 파괴 & 추매 가능 40*xrp) - ㅇ
# 5.ada 추가 숏 매수룰(하락추세룰, ma18,43 진입룰 파괴 & 추매 가능 7*ada) - ㅇ
# 6) 선물계좌 잔고 6000~12000달러 사이일때만 매수
# - 잔고부족으로 계속 매수되는 현상 방지
# -  실수로 잔고 너무 많아서 사지는것 방지

# 25/6/5 15분봉 - 15분, 60분봉-60분 쿨다운룰 추가
# 15분봉 룰은 15분이내 매매 기록을 보고, 1시간봉 룰은 1시간 이내의 매매 기록을 보고 중복 진입하는것을 방지한다.(이번 봉에서 익절 나버리면 또 진입되기 때문) 
# 롱숏 동일


# 26/6/10
# 도지룰 RSI, CLOSE 값 기준 완화. 더 잦은 매매목적
# LINK 룰 현재봉 기준 0.9% 이상 변동성+직전 lowest/highest close값 대비 0.3% 이상 변동성, 직전봉 RSI가 2% 이상 변동성 가질때 진입. 단타 목적, 직전15봉의 변동성 2.3%이상

#6/15
# xrp,ada close 룰, 하락장에서 롱진입전략은 직전 15봉 1.5% 변동성 있을때만 진입 
# high, low룰 , 15봉 변동성 1% 변동성 있을때만 진입 
# 전체 전략 15봉 변동 %에 따라 익절률 다르게 2% 미만시 익절 % 1.4%, 2% 변동성있을시 2% 익절률
# xrp, ada전략 추매 타이밍 증가 15분봉 -> 30분 이내 거래 미존재, 1시간봉은 2시간 이내 거래 미존재

#6/20 리스크 헷지
# 7% 손절 SL 주문 추가. 기존 수량있을시 tp 안거는데, 2차주문시 2차진입 기준의 tp 로  주문 수정. sl 은 최초 그대로 유지
# 5배 -> 10배 수정, 몇시간 만에 10% 이상 하락하는 경우가 1년에 2~3번 있어서, 5배로 하면 4000불 손실이라서 10배로 수정. 7% 손절 걸면 상관없는거 아닌가? 그래서 다시 5배 유지 
# cme룰 목요일도 추가


# + 추가하려는 전략
# 5캔들안에 다이버 있었는지 확인하고 1% 하락된 가격으로 진입하는 조건? 최초 다이버 이후 바로 진입될까봐 걱정, → 요건 ticker xrp 말고 다른거로 하면 되겠다.
# 추매 후 추매 물량은 tp기준으로 털고 싶은데, 그렇게 하자니 폭락시에 다 뚜드려 맞을까봐 무섭네. 차라리 7% SL이면 추가 손실은 없을거자나.
# 7% 하락하는 경우가 많이 없으니, 손절 나가면 그럴땐 그냥 2600달러 뚜두려 맞고 끝내고, 다음 abc 노리면 되지 않을까.

import time
import datetime
import ccxt
import pyupbit
import pandas as pd
import numpy as np
from datetime import timezone, timedelta


# ===================== 기본 설정 =====================

KST = timezone(timedelta(hours=9))
SOL_SYMBOL = 'SOL/USDT'
BTC_SYMBOL = 'BTC/USDT'
UPBIT_TICKER = 'KRW-SOL'
MARKET_ID_SOL = 'SOLUSDT'
MARKET_ID_BTC = 'BTCUSDT'
LEVERAGE = 5

# 바이낸스 선물 거래소 연결
exchange = ccxt.binance({
    'apiKey': 'QAK7GNH9rWZTCTaozqdNJOR9zsxB6N8QJieYRMDvXDt27ngVEwJs9tDOMAQsc1Bi',
    'secret': 'i8nNaQnZnsDL8gpAK7Q8yAWpxHZH9RYuHTY1q7ohMw9j1NXnmc1T6VCwetjfO48P',
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


# def set_margin_and_leverage(symbol):
#     """지정 심볼을 isolated 마진으로 설정하고 레버리지를 적용"""
#     exchange.load_markets()
#     exchange.set_margin_mode('isolated', symbol)
#     exchange.set_leverage(LEVERAGE, symbol)

def set_margin_and_leverage(symbol):
    exchange.load_markets()
    
    # 포지션 보유 중엔 마진 변경 불가 → 무시하고 진행
    try:
        exchange.set_margin_mode('isolated', symbol)
    except Exception as e:
        print(f"[{symbol}] 마진 모드 변경 스킵 (포지션 보유 중): {e}")
    
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

# 손절 SL 주문 추가
def place_sl_long(symbol, amount, sl_price):
    params = {
        'stopPrice': sl_price,
        'reduceOnly': True,
        'workingType': 'MARK_PRICE'
    }
    return exchange.create_order(symbol, 'STOP_MARKET', 'sell', amount, None, params)

def place_sl_short(symbol, amount, sl_price):
    params = {
        'stopPrice': sl_price,
        'reduceOnly': True,
        'workingType': 'MARK_PRICE'
    }
    return exchange.create_order(symbol, 'STOP_MARKET', 'buy', amount, None, params)

def has_position(symbol_market_id):
    """지정한 심볼의 포지션 보유 여부 확인"""
    balance = exchange.fetch_balance(params={'type': 'future'})
    positions = balance.get('info', {}).get('positions', [])
    for p in positions:
        if p.get('symbol') == symbol_market_id and abs(float(p.get('positionAmt', 0))) > 0:
            return True
    return False



# ===================== 09:00 SOL 기존 전략 =====================

def get_last_saturday_6_close():
    """가장 최근 토요일 05:00의 1시간봉 종가를 조회"""
    now = now_kst()
    sat6 = now.replace(hour=5, minute=0, second=0, microsecond=0)

    while sat6.weekday() != 5:
        sat6 -= datetime.timedelta(days=1)

    if now < sat6:
        sat6 -= datetime.timedelta(days=7)

    since_ms  = int((sat6 - datetime.timedelta(days=7)).timestamp() * 1000)
    klines    = exchange.fetch_ohlcv(SOL_SYMBOL, timeframe='1h', since=since_ms, limit=200)
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


# def get_upbit_today_open():
#     """오늘 업비트 SOL 시가 조회"""
#     df = pyupbit.get_ohlcv(UPBIT_TICKER, interval="day", count=3)
#     if df is None or len(df) < 2:
#         raise ValueError("업비트 오픈가 데이터를 가져오지 못했습니다.")
#     return float(df.iloc[-1]["open"])

def get_upbit_today_open(): # 오늘 시가는 잘 안불러와져서 어제의 종가로 불러오기로 함. 시가가 한번에 안불러와져서 오류떠서 디버깅 코드까지 추가
    """오늘 업비트 SOL 시가 조회"""
    for i in range(5):
        df = pyupbit.get_ohlcv(UPBIT_TICKER, interval="day", count=3)
        if df is not None and len(df) >= 2:
            return float(df.iloc[-2]["close"])
        print(f"재시도 {i+1}/5")
        # result = get_upbit_today_open()
        # print(f"[결과] 반환값: {result}") # 디버깅 확인용
        time.sleep(1)
    raise ValueError("업비트 데이터 실패")


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
    ma     = get_upbit_ma18_series()
    last5  = ma.iloc[-5:].tolist()
    if len(last5) < 5:
        return None

    changes = [(last5[i] / last5[i - 1] - 1) * 100 for i in range(1, 5)]

    up_3days   = changes[0] >= 0.6 and changes[1] >= 0.6 and changes[2] >= 0.6
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

    last7   = ma.iloc[-7:].tolist()
    changes = [(last7[i] / last7[i - 1] - 1) * 100 for i in range(1, 7)]

    all_up        = all(c > 0 for c in changes)
    all_down      = all(c < 0 for c in changes)
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
    if now.weekday() in [4, 5]: # 3: 목, 4: 금, 5:토, 목요일은 거래 재개
        print("금요일/토요일은 매매 금지")
        return

    if has_position(MARKET_ID_SOL):
        print("기존 SOL 포지션이 있어서 거래하지 않음")
        return

    sat_close     = get_last_saturday_6_close()
    current_price = float(exchange.fetch_ticker(SOL_SYMBOL)['last'])


    # ✅ CME 편차 1% 조건 추가
    deviation = abs(current_price - sat_close) / sat_close
    if deviation < 0.01:
        print(f"[09:00 SOL] CME 편차 {deviation*100:.2f}% 미만으로 진입 금지 "
              f"| CME={sat_close:.2f}, current={current_price:.2f}")
        return


    print(f"[09:00 SOL] CME 편차 {deviation*100:.2f}% 충족 "
          f"| CME={sat_close:.2f}, current={current_price:.2f}")


    trend = ma18_4day_change_trend()
    if trend is None:
        print("MA18 추세 데이터를 가져오지 못했습니다.")
        return

    vol_trend = ma18_6day_volatility_trend()
    if vol_trend is None:
        print("MA18 6일 변동성 추세 데이터를 가져오지 못했습니다.")
        return

    upbit_ma18, upbit_ma43         = get_upbit_ma18_ma43()
    yesterday_ma18, yesterday_ma43 = get_upbit_yesterday_ma18_ma43()
    upbit_today_open               = get_upbit_today_open()
    upbit_yesterday_open           = get_upbit_yesterday_open()

    yesterday_above_both    = upbit_yesterday_open > yesterday_ma18 and upbit_yesterday_open > yesterday_ma43
    today_below_either      = upbit_today_open < upbit_ma18 or upbit_today_open < upbit_ma43
    yesterday_not_above_both = upbit_yesterday_open <= yesterday_ma18 or upbit_yesterday_open <= yesterday_ma43
    today_above_both        = upbit_today_open > upbit_ma18 and upbit_today_open > upbit_ma43

    available_usdt = get_available_usdt()
    margin_to_use  = available_usdt * 0.5
    notional       = margin_to_use * LEVERAGE
    amount         = round(notional / current_price, 3)

    if amount <= 0:
        print("주문 수량이 0이라서 중단")
        return

    tp_price_long  = current_price * 1.0105
    tp_price_short = current_price * 0.99
    
    sl_price_long  = current_price * 0.93 
    sl_price_short = current_price * 1.07   

    print(f"[INFO] sat_close={sat_close}, current_price={current_price}")
    print(f"[UPBIT] today_open={upbit_today_open}, ma18={upbit_ma18}, ma43={upbit_ma43}")
    print(f"[YEST] yest_open={upbit_yesterday_open}, y_ma18={yesterday_ma18}, y_ma43={yesterday_ma43}")
    print(f"[TREND4] changes={trend['changes']}, up_3days={trend['up_3days']}, down_3days={trend['down_3days']}")
    print(f"[TREND6] all_up_6days={vol_trend['all_up_6days']}, all_down_6days={vol_trend['all_down_6days']}, "
          f"high_vol_days={vol_trend['high_vol_days']}")
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
        place_sl_long(SOL_SYMBOL, amount, sl_price_long)        
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
        place_sl_short(SOL_SYMBOL, amount, sl_price_short)        
        print(f"숏 진입 | amount={amount} | price={current_price} | tp={tp_price_short}")
        return

    else:
        print("진입 조건 없음")


# ===================== 메인 루프 =====================


# ===================== 확정봉 + RSI 계산 =====================

def get_confirmed_candles_with_rsi(symbol, timeframe, count=100, rsi_length=14):
    """
    현재 진행 중인 봉을 타임스탬프로 명시적으로 제거하고
    확정된 봉 기준 RSI를 Wilder(RMA) 방식으로 계산해 반환.

    count=100: RSI 수렴 정확도 확보 (과거 100봉 전 영향 0.05% 이하)
    """
    tf_ms = {
        '1m':  60_000,
        '3m':  180_000,
        '5m':  300_000,
        '15m': 900_000,
        '30m': 1_800_000,
        '1h':  3_600_000,
        '4h':  14_400_000,
        '1d':  86_400_000,
    }
    
    interval_ms = tf_ms.get(timeframe)
    if interval_ms is None:
        raise ValueError(f"지원하지 않는 타임프레임입니다: {timeframe}")    

    # count + 여유분 요청
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=count + 5)
    if ohlcv is None or len(ohlcv) < rsi_length + 16:
        raise ValueError(f"{symbol} {timeframe} 데이터가 부족합니다.")

    df = pd.DataFrame(ohlcv, columns=['ts', 'open', 'high', 'low', 'close', 'volume'])

    # 현재 진행 중인 봉 타임스탬프 계산 후 제거
    now_ms = int(datetime.datetime.now(datetime.timezone.utc).timestamp() * 1000)
    current_candle_start = (now_ms // interval_ms) * interval_ms
    df = df[df['ts'] < current_candle_start].copy()
    df = df.tail(count).reset_index(drop=True)

    if len(df) < rsi_length + 16:
        raise ValueError(f"{symbol} {timeframe} 확정봉 데이터가 부족합니다.")




    # Wilder(RMA) 방식 RSI 계산
    delta = df['close'].diff()
    gain = delta.clip(lower=0)
    loss = (-delta).clip(lower=0)

    avg_gain = pd.Series(index=df.index, dtype='float64')
    avg_loss = pd.Series(index=df.index, dtype='float64')

    avg_gain.iloc[rsi_length] = gain.iloc[1:rsi_length + 1].mean()
    avg_loss.iloc[rsi_length] = loss.iloc[1:rsi_length + 1].mean()

    for i in range(rsi_length + 1, len(df)):
        avg_gain.iloc[i] = (avg_gain.iloc[i - 1] * (rsi_length - 1) + gain.iloc[i]) / rsi_length
        avg_loss.iloc[i] = (avg_loss.iloc[i - 1] * (rsi_length - 1) + loss.iloc[i]) / rsi_length

    rs = avg_gain / avg_loss.replace(0, np.nan)
    df['rsi'] = 100 - (100 / (1 + rs))

    return df.dropna(subset=['rsi']).reset_index(drop=True)


# ===================== RSI 다이버전스 판단 =====================

# def analyze_bullish_divergence(symbol, timeframe, rsi_raise_pct=0.02, min_volatility=0.003):
    
def analyze_bullish_divergence(symbol, timeframe, rsi_raise_pct=0.02, min_volatility=0.003, price_diff_pct=0.003):
        
    """
    상승 다이버전스 조건 판단:
    - 확정봉 기준 직전봉(iloc[-1])을 판단봉으로 사용
    - 그 이전 15개 봉(iloc[-16:-1])의 lowest low보다 직전봉 close가 더 낮아야 함
    - 그 이전 15개 봉의 lowest rsi보다 직전봉 rsi가 지정 비율 이상 높아야 함
    - 직전봉 open 대비 close 변동폭이 최소 기준 이상이어야 함
    """
    df = get_confirmed_candles_with_rsi(symbol, timeframe)

    if len(df) < 16:
        return None

    prev_candle = df.iloc[-1]       # 직전 확정봉
    base_15 = df.iloc[-16:-2]  # 3~16, 2 번 봉 제외
    base_16 = df.iloc[-16:-1]  # 2~16, 2 번 봉 포함

    lowest_low = base_15['low'].min()
    lowest_rsi = base_15['rsi'].min()
    
    # ✅ 추가
    range_high = base_16['close'].max()
    range_low  = base_16['close'].min()
    range_volatility = (range_high - range_low) / range_high    

  
    cond_price      = prev_candle['close'] < lowest_low* (1 - price_diff_pct) 
    cond_rsi        = prev_candle['rsi'] >= lowest_rsi * (1 + rsi_raise_pct)
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
        "range_volatility": float(range_volatility),  # ✅ 추가        
        "tp_price": float(prev_candle['close'])
    }


def analyze_bearish_divergence(symbol, timeframe, rsi_drop_pct=0.02, min_volatility=0.003, price_diff_pct=0.003):
    """
    하락 다이버전스 조건 판단:
    - 확정봉 기준 직전봉(iloc[-1])을 판단봉으로 사용
    - 그 이전 15개 봉(iloc[-16:-1])의 highest high보다 직전봉 close가 더 높아야 함
    - 그 이전 15개 봉의 highest rsi보다 직전봉 rsi가 지정 비율 이상 낮아야 함
    - 직전봉 open 대비 close 변동폭이 최소 기준 이상이어야 함
    """
    df = get_confirmed_candles_with_rsi(symbol, timeframe)

    if len(df) < 16:
        return None

    prev_candle = df.iloc[-1]
    base_15 = df.iloc[-16:-2]  # 3~16, 2 번 봉 제외
    base_16 = df.iloc[-16:-1]  # 2~16, 2 번 봉 포함. 15봉 변동성 보는 목적


    highest_high = base_15['high'].max()
    highest_rsi  = base_15['rsi'].max()
    
    # ✅ 추가
    range_high = base_16['close'].max()
    range_low  = base_16['close'].min()
    range_volatility = (range_high - range_low) / range_high    

    cond_price      = prev_candle['close'] > highest_high * (1 + price_diff_pct)
    cond_rsi        = prev_candle['rsi'] <= highest_rsi * (1 - rsi_drop_pct)
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
        "range_volatility": float(range_volatility),  # ✅ 추가
        "tp_price": float(prev_candle['close'])
    }


# ===================== 공통 RSI 전략 실행 =====================


def trade_rsi_strategy(symbol, market_id, timeframe, tp_long_pct, tp_long_pct_2, tp_short_pct, tp_short_pct_2, min_volatility=0.003, price_diff_pct=0.003,min_range_volatility=0.01):
    """공통 RSI 다이버전스 전략 실행 함수"""
    global last_sol_trade_time, last_sol_buy_time_1h, last_sol_buy_time_15m
    
    # ──────────────────────────────────────────────────────────────
    # 쿨다운 체크 (60 초 이내 진입 금지)
    # → sleep(2) 이 실패해도 이 줄에서 2 차로 막힘
    # ──────────────────────────────────────────────────────────────
    if time.time() - last_sol_trade_time < 60:
        print(f"[{symbol} {timeframe} RSI] 60 초 쿨다운 중 진입 금지 (지난 체결 후 {time.time() - last_sol_trade_time:.1f}초 경과)")
        return
    
    # ──────────────────────────────────────────────────────────────
    # timeframe 별 쿨다운 체크 (1 시간봉=60 분, 15 분봉=15 분)
    # ──────────────────────────────────────────────────────────────
    if timeframe == '1h' and time.time() - last_sol_buy_time_1h < 3600:
        minutes_ago = (time.time() - last_sol_buy_time_1h) / 60
        print(f"[{symbol} {timeframe} RSI] 최근 {minutes_ago:.1f}분 전에 1 시간봉 매수됨 (60 분 내 중복매수 금지)")
        return
    
    if timeframe == '15m' and time.time() - last_sol_buy_time_15m < 900:
        minutes_ago = (time.time() - last_sol_buy_time_15m) / 60
        print(f"[{symbol} {timeframe} RSI] 최근 {minutes_ago:.1f}분 전에 15 분봉 매수됨 (15 분 내 중복매수 금지)")
        return
    
    set_margin_and_leverage(symbol)

    # 이미 해당 심볼 포지션이 있으면 추가 진입 금지
    if has_position(market_id):
        print(f"[{symbol} {timeframe}] 기존 포지션이 있어서 거래하지 않음")
        return

    # 선물 계좌 사용 가능 USDT 기준으로 주문 수량 계산
    available_usdt = get_available_usdt()
    margin_to_use = available_usdt * 0.5
    current_price = float(exchange.fetch_ticker(symbol)['last'])
    notional = margin_to_use * LEVERAGE
    amount = round(notional / current_price, 3)

    if amount <= 0:
        print(f"[{symbol} {timeframe}] 주문 수량이 0이라서 중단")
        return

    # 상승/하락 다이버전스 탐색
    bull = analyze_bullish_divergence(
        symbol=symbol,
        timeframe=timeframe,
        rsi_raise_pct=0.001, # 라운드 피규어 직전 직전봉(2번째봉) 제외하면 급락후 급등하는 차트에서 2번째 봉 제외하면 rsi 다이버 뜨는 경우가 종종있음. 그떄 rsi가 거의 차이가 없어서 가격차이만 있어도 되겠다고 싶음.
        min_volatility=min_volatility,
        price_diff_pct=price_diff_pct
    )
    bear = analyze_bearish_divergence(
        symbol=symbol,
        timeframe=timeframe,
        rsi_drop_pct=0.001,
        min_volatility=min_volatility,
        price_diff_pct=price_diff_pct
    )

    print(f"[{symbol} {timeframe}] BULL={bull}")
    print(f"[{symbol} {timeframe}] BEAR={bear}")

    # CME 편차 조건: 신호가 있을 때만 확인
    if (bull and bull["signal"]) or (bear and bear["signal"]):
        try:
            cme_price = get_last_saturday_6_close()
        except Exception as e:
            print(f"[{symbol} {timeframe}] 토요일 06:00 가격 조회 실패: {e}")
            return

        prev_close = bull["prev_close"] if (bull and bull["signal"]) else bear["prev_close"]
        deviation = abs(prev_close - cme_price) / cme_price

        if deviation < 0.01:
            print(f"[{symbol} {timeframe}] CME 편차 {deviation*100:.2f}% 미만으로 진입 금지 "
                  f"| CME={cme_price:.2f}, prev_close={prev_close:.2f}")
            return

        print(f"[{symbol} {timeframe}] CME 편차 {deviation*100:.2f}% 충족 "
              f"| CME={cme_price:.2f}, prev_close={prev_close:.2f}")

    # MA18 추세 필터
    trend = ma18_4day_change_trend()
    vol_trend = ma18_6day_volatility_trend()

    if trend is None or vol_trend is None:
        print(f"[{symbol} {timeframe}] MA18 추세 데이터를 가져오지 못해 중단")
        return

    # 업비트 SOL 일봉 시가와 MA18/MA43 비교값 계산
    upbit_ma18, upbit_ma43 = get_upbit_ma18_ma43()
    yesterday_ma18, yesterday_ma43 = get_upbit_yesterday_ma18_ma43()
    upbit_today_open = get_upbit_today_open()
    upbit_yesterday_open = get_upbit_yesterday_open()

    # 어제 시가가 둘 다 위에 있었는지
    yesterday_above_both = (
        upbit_yesterday_open > yesterday_ma18 and
        upbit_yesterday_open > yesterday_ma43
    )

    # 어제 시가가 둘 다 아래에 있었는지
    yesterday_below_both = (
        upbit_yesterday_open < yesterday_ma18 and
        upbit_yesterday_open < yesterday_ma43
    )

    # 오늘 시가가 둘 다 위로 돌파했는지
    today_above_both = (
        upbit_today_open > upbit_ma18 and
        upbit_today_open > upbit_ma43
    )

    # 오늘 시가가 둘 중 하나라도 아래로 깨졌는지
    today_below_either = (
        upbit_today_open < upbit_ma18 or
        upbit_today_open < upbit_ma43
    )

    print(f"[{symbol} {timeframe}] TREND4={trend['changes']}, up={trend['up_3days']}, down={trend['down_3days']}")
    print(f"[{symbol} {timeframe}] TREND6 all_up={vol_trend['all_up_6days']}, all_down={vol_trend['all_down_6days']}, high_vol={vol_trend['high_vol_days']}")

    # 손절 주문 7%
    sl_pct = 0.07
    
    # 롱 신호 처리
    if bull and bull["signal"]:
        if bull["range_volatility"] < min_range_volatility:
            print(f"[{symbol} {timeframe}] range_volatility {bull['range_volatility']*100:.2f}% 로 1% 미만이라 롱 진입 금지")
            return

        if yesterday_above_both and today_below_either:
            print(f"[{symbol} {timeframe}] 어제 MA 위 → 오늘 MA 아래 전환으로 롱 진입 금지")
            return

        if trend["down_3days"]:
            print(f"[{symbol} {timeframe}] MA18 3 일 연속 하락으로 롱 진입 금지")
            return

        if vol_trend["all_down_6days"] and vol_trend["high_vol_days"] >= 5:
            print(f"[{symbol} {timeframe}] MA18 6 일 연속 하락 + 고변동 5 일이상으로 롱 진입 금지")
            return

        tp_pct = tp_long_pct_2 if bull["range_volatility"] > 0.02 else tp_long_pct
        tp_price = bull["prev_close"] * (1 + tp_pct)
        sl_price = bull["prev_close"] * (1 - sl_pct)
        exchange.create_market_buy_order(symbol, amount)
        
        # ──────────────────────────────────────────────────────────────
        # 매수 실행 직후 시간 기록 (쿨다운용)
        # ──────────────────────────────────────────────────────────────
        last_sol_trade_time = time.time()
        if timeframe == '1h':
            last_sol_buy_time_1h = time.time()
        elif timeframe == '15m':
            last_sol_buy_time_15m = time.time()
        
        place_tp_long(symbol, amount, tp_price)
        place_sl_long(symbol, amount, sl_price)
        print(f"[{symbol} {timeframe}] 롱 진입 | amount={amount} | price={current_price} | tp={tp_price}")
        return

    # 숏 신호 처리
    if bear and bear["signal"]:
        if bear["range_volatility"] < min_range_volatility:
            print(f"[{symbol} {timeframe}] range_volatility {bear['range_volatility']*100:.2f}% 로 1% 미만이라 숏 진입 금지")
            return

        if yesterday_below_both and today_above_both:
            print(f"[{symbol} {timeframe}] 어제 MA 아래 → 오늘 MA 위 돌파로 숏 진입 금지")
            return

        if trend["up_3days"]:
            print(f"[{symbol} {timeframe}] MA18 3 일 연속 상승으로 숏 진입 금지")
            return

        if vol_trend["all_up_6days"] and vol_trend["high_vol_days"] >= 5:
            print(f"[{symbol} {timeframe}] MA18 6 일 연속 상승 + 고변동 5 일이상으로 숏 진입 금지")
            return

        tp_pct = tp_short_pct_2 if bear["range_volatility"] > 0.02 else tp_short_pct
        tp_price = bear["prev_close"] * (1 - tp_pct)
        sl_price = bear["prev_close"] * (1 + sl_pct)
        exchange.create_market_sell_order(symbol, amount)

        # ──────────────────────────────────────────────────────────────
        # 매수 실행 직후 시간 기록 (쿨다운용)
        # ──────────────────────────────────────────────────────────────
        last_sol_trade_time = time.time()
        if timeframe == '1h':
            last_sol_buy_time_1h = time.time()
        elif timeframe == '15m':
            last_sol_buy_time_15m = time.time()

        place_tp_short(symbol, amount, tp_price)
        place_sl_short(symbol, amount, sl_price)
        print(f"[{symbol} {timeframe}] 숏 진입 | amount={amount} | price={current_price} | tp={tp_price}")
        return

    print(f"[{symbol} {timeframe}] 진입 조건 없음")


#---------------- lowest close 값도 있어야지 완화된 룰 다만 신뢰도가 낮을 수 있음
def analyze_bullish_divergence_close(symbol, timeframe, rsi_raise_pct=0.02, min_volatility=0.003, price_diff_pct=0.001):
    """
    상승 다이버전스 조건 판단 (close 기준 - 완화된 룰):
    """
    df = get_confirmed_candles_with_rsi(symbol, timeframe)

    if len(df) < 16:
        return None

    prev_candle = df.iloc[-1]  # 직전봉 1
    base_15 = df.iloc[-16:-2]  # 3~16, 2 번 봉 제외
    base_16 = df.iloc[-16:-1]  # 2~16, 2 번 봉 포함

    lowest_close = base_15['close'].min()
    lowest_rsi = base_15['rsi'].min()
    
    # ✅ 추가
    range_high = base_16['close'].max()
    range_low  = base_16['close'].min()
    range_volatility = (range_high - range_low) / range_high    

    cond_price = prev_candle['close'] < lowest_close * (1 - price_diff_pct)
    cond_rsi = prev_candle['rsi'] >= lowest_rsi * (1 + rsi_raise_pct)
    cond_volatility = abs(prev_candle['close'] - prev_candle['open']) / prev_candle['open'] >= min_volatility

    signal = cond_price and cond_rsi and cond_volatility

    return {
        "signal": signal,
        "side": "long",
        "lowest_close": float(lowest_close),
        "lowest_rsi": float(lowest_rsi),
        "prev_open": float(prev_candle['open']),
        "prev_close": float(prev_candle['close']),
        "prev_rsi": float(prev_candle['rsi']),
        "price_condition": cond_price,
        "rsi_condition": cond_rsi,
        "volatility_condition": cond_volatility,
        "range_volatility": float(range_volatility),  # ✅ 추가        
        "tp_price": float(prev_candle['close'])
    }


def analyze_bearish_divergence_close(symbol, timeframe, rsi_drop_pct=0.02, min_volatility=0.003, price_diff_pct=0.001):
    """
    하락 다이버전스 조건 판단 (close 기준 - 완화된 룰):
    """
    df = get_confirmed_candles_with_rsi(symbol, timeframe)

    if len(df) < 16:
        return None

    prev_candle = df.iloc[-1]  # 직전봉 1
    base_15 = df.iloc[-16:-2]  # 3~16, 2 번 봉 제외
    base_16 = df.iloc[-16:-1]  # 2~16, 2 번 봉 포함

    highest_close = base_15['close'].max()
    highest_rsi = base_15['rsi'].max()
    
    # ✅ 추가
    range_high = base_16['close'].max()
    range_low  = base_16['close'].min()
    range_volatility = (range_high - range_low) / range_high    

    cond_price = prev_candle['close'] > highest_close * (1 + price_diff_pct)
    cond_rsi = prev_candle['rsi'] <= highest_rsi * (1 - rsi_drop_pct)
    cond_volatility = abs(prev_candle['close'] - prev_candle['open']) / prev_candle['open'] >= min_volatility

    signal = cond_price and cond_rsi and cond_volatility

    return {
        "signal": signal,
        "side": "short",
        "highest_close": float(highest_close),
        "highest_rsi": float(highest_rsi),
        "prev_open": float(prev_candle['open']),
        "prev_close": float(prev_candle['close']),
        "prev_rsi": float(prev_candle['rsi']),
        "price_condition": cond_price,
        "rsi_condition": cond_rsi,
        "volatility_condition": cond_volatility,
        "range_volatility": float(range_volatility),  # ✅ 추가       
        "tp_price": float(prev_candle['close'])
    }


def trade_rsi_close_strategy(symbol, market_id, timeframe, tp_long_pct, tp_long_pct_2, tp_short_pct, tp_short_pct_2, min_volatility=0.003, price_diff_pct=0.001, rsi_raise_pct=0.003, rsi_drop_pct=0.003):
    """close 기준 RSI 다이버전스 전략 실행 함수 (롱 + 숏)"""
    global last_sol_trade_time, last_sol_buy_time_1h, last_sol_buy_time_15m

    # ──────────────────────────────────────────────────────────────
    # 쿨다운 체크 (60 초 이내 진입 금지)
    # ──────────────────────────────────────────────────────────────
    if time.time() - last_sol_trade_time < 60:
        print(f"[{symbol} {timeframe} RSI_CLOSE] 60 초 쿨다운 중 진입 금지 (지난 체결 후 {time.time() - last_sol_trade_time:.1f}초 경과)")
        return

    # ──────────────────────────────────────────────────────────────
    # timeframe 별 쿨다운 체크 (1 시간봉=60 분, 15 분봉=15 분)
    # ──────────────────────────────────────────────────────────────
    if timeframe == '1h' and time.time() - last_sol_buy_time_1h < 3600:
        minutes_ago = (time.time() - last_sol_buy_time_1h) / 60
        print(f"[{symbol} {timeframe} RSI_CLOSE] 최근 {minutes_ago:.1f}분 전에 1 시간봉 매수됨 (60 분 내 중복매수 금지)")
        return

    if timeframe == '15m' and time.time() - last_sol_buy_time_15m < 900:
        minutes_ago = (time.time() - last_sol_buy_time_15m) / 60
        print(f"[{symbol} {timeframe} RSI_CLOSE] 최근 {minutes_ago:.1f}분 전에 15 분봉 매수됨 (15 분 내 중복매수 금지)")
        return

    set_margin_and_leverage(symbol)

    # 이미 해당 심볼 포지션이 있으면 추가 진입 금지
    if has_position(market_id):
        print(f"[{symbol} {timeframe}] 기존 포지션이 있어서 거래하지 않음")
        return

    # 선물 계좌 사용 가능 USDT 기준으로 주문 수량 계산
    available_usdt = get_available_usdt()
    margin_to_use = available_usdt * 0.5
    current_price = float(exchange.fetch_ticker(symbol)['last'])
    notional = margin_to_use * LEVERAGE
    amount = round(notional / current_price, 3)

    if amount <= 0:
        print(f"[{symbol} {timeframe}] 주문 수량이 0 이라서 중단")
        return

    # close 기준 상승/하락 다이버전스 탐색
    # rsi_raise_pct, rsi_drop_pct, price_diff_pct 모두 숫자 직접 입력
    bull_close = analyze_bullish_divergence_close(
        symbol=symbol,
        timeframe=timeframe,
        rsi_raise_pct=rsi_raise_pct,
        min_volatility=min_volatility,
        price_diff_pct=price_diff_pct
    )

    bear_close = analyze_bearish_divergence_close(
        symbol=symbol,
        timeframe=timeframe,
        rsi_drop_pct=rsi_drop_pct,
        min_volatility=min_volatility,
        price_diff_pct=price_diff_pct
    )

    print(f"[{symbol} {timeframe}] BULL_CLOSE={bull_close}")
    print(f"[{symbol} {timeframe}] BEAR_CLOSE={bear_close}")

    # CME 편차 조건: 신호가 있을 때만 확인
    if (bull_close and bull_close["signal"]) or (bear_close and bear_close["signal"]):
        try:
            cme_price = get_last_saturday_6_close()
        except Exception as e:
            print(f"[{symbol} {timeframe}] 토요일 06:00 가격 조회 실패: {e}")
            return

        prev_close = (
            bull_close["prev_close"] if (bull_close and bull_close["signal"])
            else bear_close["prev_close"]
        )
        deviation = abs(prev_close - cme_price) / cme_price

        if deviation < 0.01:
            print(f"[{symbol} {timeframe}] CME 편차 {deviation*100:.2f}% 미만으로 진입 금지 "
                  f"| CME={cme_price:.2f}, prev_close={prev_close:.2f}")
            return

        print(f"[{symbol} {timeframe}] CME 편차 {deviation*100:.2f}% 충족 "
              f"| CME={cme_price:.2f}, prev_close={prev_close:.2f}")

    # MA18 추세 필터
    trend = ma18_4day_change_trend()
    vol_trend = ma18_6day_volatility_trend()

    if trend is None or vol_trend is None:
        print(f"[{symbol} {timeframe}] MA18 추세 데이터를 가져오지 못해 중단")
        return

    # 업비트 SOL 일봉 시가와 MA18/MA43 비교값 계산
    upbit_ma18, upbit_ma43 = get_upbit_ma18_ma43()
    yesterday_ma18, yesterday_ma43 = get_upbit_yesterday_ma18_ma43()
    upbit_today_open = get_upbit_today_open()
    upbit_yesterday_open = get_upbit_yesterday_open()

    # 어제 시가가 둘 다 위에 있었는지
    yesterday_above_both = (
        upbit_yesterday_open > yesterday_ma18 and
        upbit_yesterday_open > yesterday_ma43
    )

    # 어제 시가가 둘 다 아래에 있었는지
    yesterday_below_both = (
        upbit_yesterday_open < yesterday_ma18 and
        upbit_yesterday_open < yesterday_ma43
    )

    # 오늘 시가가 둘 다 위로 돌파했는지
    today_above_both = (
        upbit_today_open > upbit_ma18 and
        upbit_today_open > upbit_ma43
    )

    # 오늘 시가가 둘 중 하나라도 아래로 깨졌는지
    today_below_either = (
        upbit_today_open < upbit_ma18 or
        upbit_today_open < upbit_ma43
    )

    print(f"[{symbol} {timeframe}] TREND4={trend['changes']}, up={trend['up_3days']}, down={trend['down_3days']}")
    print(f"[{symbol} {timeframe}] TREND6 all_up={vol_trend['all_up_6days']}, all_down={vol_trend['all_down_6days']}, high_vol={vol_trend['high_vol_days']}")

    sl_pct = 0.07
    # 롱 신호 처리
    if bull_close and bull_close["signal"]:
        # 업비트 조건: 어제 MA 위였는데 오늘 MA 아래로 깨지면 롱 금지
        if yesterday_above_both and today_below_either:
            print(f"[{symbol} {timeframe}] 어제 MA 위 → 오늘 MA 아래 전환으로 롱 진입 금지")
            return

        if trend["down_3days"]:
            print(f"[{symbol} {timeframe}] MA18 3 일 연속 하락으로 롱 진입 금지")
            return

        if vol_trend["all_down_6days"] and vol_trend["high_vol_days"] >= 5:
            print(f"[{symbol} {timeframe}] MA18 6 일 연속 하락 + 고변동 5 일이상으로 롱 진입 금지")
            return

        tp_pct = tp_long_pct_2 if bull_close["range_volatility"] > 0.02 else tp_long_pct
        tp_price = bull_close["prev_close"] * (1 + tp_pct)
        sl_price = bull_close["prev_close"] * (1 - sl_pct)
        exchange.create_market_buy_order(symbol, amount)

        # ──────────────────────────────────────────────────────────────
        # 매수 실행 직후 시간 기록 (쿨다운용)
        # ──────────────────────────────────────────────────────────────
        last_sol_trade_time = time.time()
        if timeframe == '1h':
            last_sol_buy_time_1h = time.time()
        elif timeframe == '15m':
            last_sol_buy_time_15m = time.time()

        place_tp_long(symbol, amount, tp_price)
        place_sl_long(symbol, amount, sl_price)
        print(f"[{symbol} {timeframe}] CLOSE 기준 롱 진입 | amount={amount} | price={current_price} | tp={tp_price}")
        return

    # 숏 신호 처리
    if bear_close and bear_close["signal"]:
        # 업비트 조건: 어제 MA 아래였는데 오늘 MA 위로 돌파하면 숏 금지
        if yesterday_below_both and today_above_both:
            print(f"[{symbol} {timeframe}] 어제 MA 아래 → 오늘 MA 위 전환으로 숏 진입 금지")
            return

        if trend["up_3days"]:
            print(f"[{symbol} {timeframe}] MA18 3 일 연속 상승으로 숏 진입 금지")
            return

        if vol_trend["all_up_6days"] and vol_trend["high_vol_days"] >= 5:
            print(f"[{symbol} {timeframe}] MA18 6 일 연속 상승 + 고변동 5 일이상으로 숏 진입 금지")
            return

        tp_pct = tp_short_pct_2 if bear_close["range_volatility"] > 0.02 else tp_short_pct
        tp_price = bear_close["prev_close"] * (1 - tp_pct)
        sl_price = bear_close["prev_close"] * (1 + sl_pct)
        exchange.create_market_sell_order(symbol, amount)

        # ──────────────────────────────────────────────────────────────
        # 매수 실행 직후 시간 기록 (쿨다운용)
        # ──────────────────────────────────────────────────────────────
        last_sol_trade_time = time.time()
        if timeframe == '1h':
            last_sol_buy_time_1h = time.time()
        elif timeframe == '15m':
            last_sol_buy_time_15m = time.time()

        place_tp_short(symbol, amount, tp_price)
        place_sl_short(symbol, amount, sl_price)        
        print(f"[{symbol} {timeframe}] CLOSE 기준 숏 진입 | amount={amount} | price={current_price} | tp={tp_price}")
        return

    print(f"[{symbol} {timeframe}] CLOSE 기준 진입 조건 없음")

#------ 제약 파괴후 추매 룰
# 코인 잔고 개수 불러오는 함수 
def get_position_amount(symbol):
    """특정 심볼의 포지션 수량 반환 (양수=롱, 음수=숏, 0=없음)"""
    balance = exchange.fetch_balance(params={'type': 'future'})
    positions = balance.get('info', {}).get('positions', [])
    for p in positions:
        if p.get('symbol') == symbol.replace('/', ''):
            amt = float(p.get('positionAmt', 0))
            return amt
    return 0


def trade_rsi_close_strategy_xrp_long(
    symbol,
    market_id,
    timeframe,
    tp_long_pct,
    tp_long_pct_2=None,
    min_volatility=0.003,
    price_diff_pct=0.001,
    rsi_raise_pct=0.003,
    min_range_volatility=0.015
):
    """
    XRP 보유 시 롱 조건만 적용.
    TP 분기 유지:
      - range_volatility > 0.018 이면 tp_long_pct_2
      - 아니면 tp_long_pct
    진입 제약:
      - range_volatility >= 0.015 일 때만 진입
    """
    global last_xrp_long_trade_time, last_xrp_long_1h, last_xrp_long_15m

    if time.time() - last_xrp_long_trade_time < 60:
        print(f"[{symbol} XRP_LONG] 60 초 쿨다운 중 진입 금지 (지난 체결 후 {time.time() - last_xrp_long_trade_time:.1f}초 경과)")
        return

    if timeframe == '1h' and time.time() - last_xrp_long_1h < 10800:
        minutes_ago = (time.time() - last_xrp_long_1h) / 60
        print(f"[{symbol} XRP_LONG 1h] 최근 {minutes_ago:.1f}분 전에 1 시간봉 매수됨 (180 분 내 중복매수 금지)")
        return

    if timeframe == '15m' and time.time() - last_xrp_long_15m < 2700:
        minutes_ago = (time.time() - last_xrp_long_15m) / 60
        print(f"[{symbol} XRP_LONG 15m] 최근 {minutes_ago:.1f}분 전에 15 분봉 매수됨 (45 분 내 중복매수 금지)")
        return

    set_margin_and_leverage(symbol)
    current_balance = get_available_usdt()

    if current_balance < 5500 or current_balance > 12000:
        print(f"[{symbol} XRP_LONG] 계좌 잔고 {current_balance:.2f} USD (6000~12000 밖이므로 진입 금지)")
        return

    xrp_position = get_position_amount('XRP/USDT')
    if xrp_position <= 0:
        print(f"[{symbol} XRP_LONG] XRP 포지션 없음 (롱 진입 금지)")
        return

    n_xrp = abs(xrp_position)
    sol_threshold = 40 * n_xrp
    sol_position = get_position_amount('SOL/USDT')
    current_sol = sol_position if sol_position > 0 else 0

    print(f"[{symbol} XRP_LONG] XRP 보유량: {n_xrp}개, SOL 보유량: {current_sol}개, 기준치: {sol_threshold}개")

    if current_sol > sol_threshold:
        print(f"[{symbol} XRP_LONG] SOL 보유량 {current_sol}개 > 기준 {sol_threshold}개로 매수 금지")
        return

    current_price = float(exchange.fetch_ticker(symbol)['last'])
    available_usdt = get_available_usdt()
    margin_to_use = available_usdt * 0.5
    notional = margin_to_use * LEVERAGE
    amount = round(notional / current_price, 3)

    if amount <= 0:
        print(f"[{symbol} XRP_LONG] 주문 수량이 0 이라서 중단")
        return

    bull_close = analyze_bullish_divergence_close(
        symbol=symbol,
        timeframe=timeframe,
        rsi_raise_pct=rsi_raise_pct,
        min_volatility=min_volatility,
        price_diff_pct=price_diff_pct
    )

    print(f"[{symbol} XRP_LONG] BULL_CLOSE={bull_close}")

    if not bull_close or not bull_close["signal"]:
        print(f"[{symbol} XRP_LONG] CLOSE 기준 진입 조건 없음")
        return

    if bull_close["range_volatility"] < min_range_volatility:
        print(f"[{symbol} XRP_LONG] range_volatility {bull_close['range_volatility']*100:.2f}% 미만으로 진입 금지")
        return

    try:
        cme_price = get_last_saturday_6_close()
    except Exception as e:
        print(f"[{symbol} XRP_LONG] 토요일 06:00 가격 조회 실패: {e}")
        return

    deviation = abs(bull_close["prev_close"] - cme_price) / cme_price
    if deviation < 0.01:
        print(f"[{symbol} XRP_LONG] CME 편차 {deviation*100:.2f}% 미만으로 진입 금지 | CME={cme_price:.2f}, prev_close={bull_close['prev_close']:.2f}")
        return

    print(f"[{symbol} XRP_LONG] CME 편차 {deviation*100:.2f}% 충족 | CME={cme_price:.2f}, prev_close={bull_close['prev_close']:.2f}")

    tp_pct = tp_long_pct_2 if (tp_long_pct_2 is not None and bull_close["range_volatility"] > 0.018) else tp_long_pct
    tp_price = bull_close["prev_close"] * (1 + tp_pct)
    sl_price = bull_close["prev_close"] * (1 - 0.07)
    exchange.create_market_buy_order(symbol, amount)

    last_xrp_long_trade_time = time.time()
    if timeframe == '1h':
        last_xrp_long_1h = time.time()
    elif timeframe == '15m':
        last_xrp_long_15m = time.time()


    if current_sol == 0:
        place_tp_long(symbol, amount, tp_price)
        place_sl_long(symbol, amount, sl_price)    
        print(f"[{symbol} XRP_LONG] CLOSE 기준 롱 진입 (첫 매매, TP 걸림) | amount={amount} | price={current_price} | tp={tp_price} | tp_pct={tp_pct}")
    else:
        print(f"[{symbol} XRP_LONG] CLOSE 기준 롱 진입 (추가 매수, TP 없음) | amount={amount} | price={current_price}")



def trade_rsi_close_strategy_ada_short(
    symbol,
    market_id,
    timeframe,
    tp_short_pct,
    tp_short_pct_2=None,
    min_volatility=0.003,
    price_diff_pct=0.001,
    rsi_drop_pct=0.003,
    min_range_volatility=0.015
):
    """
    ADA 보유 시 숏 조건만 적용.
    TP 분기 유지:
      - range_volatility > 0.018 이면 tp_short_pct_2
      - 아니면 tp_short_pct
    진입 제약:
      - range_volatility >= 0.015 일 때만 진입
    """
    global last_ada_short_trade_time, last_ada_short_1h, last_ada_short_15m

    if time.time() - last_ada_short_trade_time < 60:
        print(f"[{symbol} ADA_SHORT] 60 초 쿨다운 중 진입 금지 (지난 체결 후 {time.time() - last_ada_short_trade_time:.1f}초 경과)")
        return

    if timeframe == '1h' and time.time() - last_ada_short_1h < 10800:
        minutes_ago = (time.time() - last_ada_short_1h) / 60
        print(f"[{symbol} ADA_SHORT 1h] 최근 {minutes_ago:.1f}분 전에 1 시간봉 매수됨 (180 분 내 중복매수 금지)")
        return

    if timeframe == '15m' and time.time() - last_ada_short_15m < 2700:
        minutes_ago = (time.time() - last_ada_short_15m) / 60
        print(f"[{symbol} ADA_SHORT 15m] 최근 {minutes_ago:.1f}분 전에 15 분봉 매수됨 (45 분 내 중복매수 금지)")
        return

    set_margin_and_leverage(symbol)
    current_balance = get_available_usdt()

    if current_balance < 4000 or current_balance > 14000:
        print(f"[{symbol} ADA_SHORT] 계좌 잔고 {current_balance:.2f} USD (6000~12000 밖이므로 진입 금지)")
        return

    ada_position = get_position_amount('ADA/USDT')
    if ada_position >= 0:
        print(f"[{symbol} ADA_SHORT] ADA 숏 포지션 없음 (숏 진입 금지)")
        return

    n_ada = abs(ada_position)
    sol_threshold = 7 * n_ada
    sol_position = get_position_amount('SOL/USDT')
    current_sol = -sol_position if sol_position < 0 else 0

    print(f"[{symbol} ADA_SHORT] ADA 숏 보유량: {n_ada}개, SOL 숏 보유량: {current_sol}개, 기준치: {sol_threshold}개")

    if current_sol > sol_threshold:
        print(f"[{symbol} ADA_SHORT] SOL 숏 보유량 {current_sol}개 > 기준 {sol_threshold}개로 매수 금지")
        return

    current_price = float(exchange.fetch_ticker(symbol)['last'])
    available_usdt = get_available_usdt()
    margin_to_use = available_usdt * 0.5
    notional = margin_to_use * LEVERAGE
    amount = round(notional / current_price, 3)

    if amount <= 0:
        print(f"[{symbol} ADA_SHORT] 주문 수량이 0 이라서 중단")
        return

    bear_close = analyze_bearish_divergence_close(
        symbol=symbol,
        timeframe=timeframe,
        rsi_drop_pct=rsi_drop_pct,
        min_volatility=min_volatility,
        price_diff_pct=price_diff_pct
    )

    print(f"[{symbol} ADA_SHORT] BEAR_CLOSE={bear_close}")

    if not bear_close or not bear_close["signal"]:
        print(f"[{symbol} ADA_SHORT] CLOSE 기준 진입 조건 없음")
        return

    if bear_close["range_volatility"] < min_range_volatility:
        print(f"[{symbol} ADA_SHORT] range_volatility {bear_close['range_volatility']*100:.2f}% 미만으로 진입 금지")
        return

    try:
        cme_price = get_last_saturday_6_close()
    except Exception as e:
        print(f"[{symbol} ADA_SHORT] 토요일 06:00 가격 조회 실패: {e}")
        return

    deviation = abs(bear_close["prev_close"] - cme_price) / cme_price
    if deviation < 0.01:
        print(f"[{symbol} ADA_SHORT] CME 편차 {deviation*100:.2f}% 미만으로 진입 금지 | CME={cme_price:.2f}, prev_close={bear_close['prev_close']:.2f}")
        return

    print(f"[{symbol} ADA_SHORT] CME 편차 {deviation*100:.2f}% 충족 | CME={cme_price:.2f}, prev_close={bear_close['prev_close']:.2f}")

    tp_pct = tp_short_pct_2 if (tp_short_pct_2 is not None and bear_close["range_volatility"] > 0.018) else tp_short_pct
    tp_price = bear_close["prev_close"] * (1 - tp_pct)
    sl_price = bear_close["prev_close"] * (1 + 0.07)
    exchange.create_market_sell_order(symbol, amount)

    last_ada_short_trade_time = time.time()
    if timeframe == '1h':
        last_ada_short_1h = time.time()
    elif timeframe == '15m':
        last_ada_short_15m = time.time()

    if current_sol == 0:
        place_tp_short(symbol, amount, tp_price)
        place_sl_short(symbol, amount, sl_price)
        print(f"[{symbol} ADA_SHORT] CLOSE 기준 숏 진입 (첫 매매, TP 걸림) | amount={amount} | price={current_price} | tp={tp_price} | tp_pct={tp_pct}")
    else:
        print(f"[{symbol} ADA_SHORT] CLOSE 기준 숏 진입 (추가 매수, TP 없음) | amount={amount} | price={current_price}")

# 도지 전략 추가, 급락 후 rsi, close diff pct 완화해서 사용하는 목적
def trade_rsi_close_strategy_doge(symbol, market_id, timeframe, tp_long_pct, tp_short_pct, min_volatility=0.003, price_diff_pct=0.001, rsi_raise_pct=0.003, rsi_drop_pct=0.003):
    """
    DOGE 보유 시 롱 + 숏 조건 적용 (제약룰 무시, CME 조건은 유지)
    DOGE 보유 시에만 실행, SOL 포지션 있으면 진입 금지
    ✅ 첫 매매 (SOL 0 개) → TP 걸기
    ✅ 추가 매수 (SOL > 0 개) → TP 안 걸기
    """

    global last_sol_trade_time, last_sol_buy_time_1h, last_sol_buy_time_15m

    # ──────────────────────────────────────────────────────────────
    # SOL 포지션 체크: 있으면 진입 금지
    # ──────────────────────────────────────────────────────────────
    if has_position(MARKET_ID_SOL):
        print(f"[{symbol} DOGE] SOL 포지션 있음으로 진입 금지")
        return

    # ──────────────────────────────────────────────────────────────
    # 쿨다운 체크 (60 초 이내 진입 금지)
    # ──────────────────────────────────────────────────────────────
    if time.time() - last_sol_trade_time < 60:
        print(f"[{symbol} DOGE] 60 초 쿨다운 중 진입 금지 (지난 체결 후 {time.time() - last_sol_trade_time:.1f}초 경과)")
        return

    # ──────────────────────────────────────────────────────────────
    # timeframe 별 쿨다운 체크 (1 시간봉=60 분, 15 분봉=15 분)
    # ──────────────────────────────────────────────────────────────
    if timeframe == '1h' and time.time() - last_sol_buy_time_1h < 3600:
        minutes_ago = (time.time() - last_sol_buy_time_1h) / 60
        print(f"[{symbol} DOGE 1h] 최근 {minutes_ago:.1f}분 전에 1 시간봉 매수됨 (60 분 내 중복매수 금지)")
        return

    if timeframe == '15m' and time.time() - last_sol_buy_time_15m < 900:
        minutes_ago = (time.time() - last_sol_buy_time_15m) / 60
        print(f"[{symbol} DOGE 15m] 최근 {minutes_ago:.1f}분 전에 15 분봉 매수됨 (15 분 내 중복매수 금지)")
        return

    set_margin_and_leverage(symbol)

    # DOGE 포지션 확인 (보유 여부만 확인, 개수는 기준치 없음)
    doge_position = get_position_amount('DOGE/USDT')
    if doge_position == 0:
        print(f"[{symbol} DOGE] DOGE 보유 없음 (진입 금지)")
        return

    print(f"[{symbol} DOGE] DOGE 보유량: {doge_position}개")

    # 선물 계좌 사용 가능 USDT 기준으로 주문 수량 계산
    available_usdt = get_available_usdt()
    margin_to_use = available_usdt * 0.5
    current_price = float(exchange.fetch_ticker(symbol)['last'])
    notional = margin_to_use * LEVERAGE
    amount = round(notional / current_price, 3)

    if amount <= 0:
        print(f"[{symbol} DOGE] 주문 수량이 0 이라서 중단")
        return

    # close 기준 상승/하락 다이버전스 탐색
    bull_close = analyze_bullish_divergence_close(
        symbol=symbol,
        timeframe=timeframe,
        rsi_raise_pct=rsi_raise_pct,
        min_volatility=min_volatility,
        price_diff_pct=price_diff_pct
    )

    bear_close = analyze_bearish_divergence_close(
        symbol=symbol,
        timeframe=timeframe,
        rsi_drop_pct=rsi_drop_pct,
        min_volatility=min_volatility,
        price_diff_pct=price_diff_pct
    )

    print(f"[{symbol} DOGE] BULL_CLOSE={bull_close}")
    print(f"[{symbol} DOGE] BEAR_CLOSE={bear_close}")

    # CME 편차 조건: 신호가 있을 때만 확인
    if (bull_close and bull_close["signal"]) or (bear_close and bear_close["signal"]):
        try:
            cme_price = get_last_saturday_6_close()
        except Exception as e:
            print(f"[{symbol} DOGE] 토요일 06:00 가격 조회 실패: {e}")
            return

        prev_close = (
            bull_close["prev_close"] if (bull_close and bull_close["signal"])
            else bear_close["prev_close"]
        )
        deviation = abs(prev_close - cme_price) / cme_price

        if deviation < 0.01:
            print(f"[{symbol} DOGE] CME 편차 {deviation*100:.2f}% 미만으로 진입 금지 "
                  f"| CME={cme_price:.2f}, prev_close={prev_close:.2f}")
            return

        print(f"[{symbol} DOGE] CME 편차 {deviation*100:.2f}% 충족 "
              f"| CME={cme_price:.2f}, prev_close={prev_close:.2f}")

    # 현재 SOL 보유량 확인 (첫 매매 vs 추가매수 판단)
    sol_position = get_position_amount('SOL/USDT')
    current_sol = sol_position if sol_position > 0 else 0

    # 롱 신호 처리 (제약룰 모두 제거)
    if bull_close and bull_close["signal"]:
        tp_price = bull_close["prev_close"] * (1 + tp_long_pct)
        exchange.create_market_buy_order(symbol, amount)

        # ──────────────────────────────────────────────────────────────
        # 매수 실행 직후 시간 기록 (쿨다운용)
        # ──────────────────────────────────────────────────────────────
        last_sol_trade_time = time.time()
        if timeframe == '1h':
            last_sol_buy_time_1h = time.time()
        elif timeframe == '15m':
            last_sol_buy_time_15m = time.time()

        # ✅ 첫 매매 (SOL 0 개) → TP 걸기, 추가 매수 (SOL > 0 개) → TP 안 걸기
        if current_sol == 0:
            place_tp_long(symbol, amount, tp_price)
            print(f"[{symbol} DOGE] CLOSE 기준 롱 진입 (첫 매매, TP 걸림) | amount={amount} | price={current_price} | tp={tp_price}")
        else:
            print(f"[{symbol} DOGE] CLOSE 기준 롱 진입 (추가 매수, TP 없음) | amount={amount} | price={current_price}")
        return

    # 숏 신호 처리 (제약룰 모두 제거)
    if bear_close and bear_close["signal"]:
        tp_price = bear_close["prev_close"] * (1 - tp_short_pct)
        exchange.create_market_sell_order(symbol, amount)

        # ──────────────────────────────────────────────────────────────
        # 매수 실행 직후 시간 기록 (쿨다운용)
        # ──────────────────────────────────────────────────────────────
        last_sol_trade_time = time.time()
        if timeframe == '1h':
            last_sol_buy_time_1h = time.time()
        elif timeframe == '15m':
            last_sol_buy_time_15m = time.time()

        # ✅ 첫 매매 (SOL 0 개) → TP 걸기, 추가 매수 (SOL > 0 개) → TP 안 걸기
        if current_sol == 0:
            place_tp_short(symbol, amount, tp_price)
            print(f"[{symbol} DOGE] CLOSE 기준 숏 진입 (첫 매매, TP 걸림) | amount={amount} | price={current_price} | tp={tp_price}")
        else:
            print(f"[{symbol} DOGE] CLOSE 기준 숏 진입 (추가 매수, TP 없음) | amount={amount} | price={current_price}")
        return

    print(f"[{symbol} DOGE] CLOSE 기준 진입 조건 없음")


# 링크 전략 추가, 급락 후 rsi, close diff pct 완화+ 현재가 기준 -0.9% 조건 만족시 봉 마감 전에 바로 진입
# ──────────────────────────────────────────────────────────────
# 2. 수정된 CHAINLINK (LINK) 전략 (현재봉 0.9% + 다이버전스 듀얼)
# ──────────────────────────────────────────────────────────────
def trade_current_bar_09_pct_strategy(symbol, market_id, timeframe, tp_long_pct, tp_short_pct, 
                                       min_volatility=0.003, current_bar_pct=0.009,
                                       price_diff_pct=0.001, rsi_raise_pct=0.003, rsi_drop_pct=0.003,
                                       range_volatility_pct=0.023):
    """
    CHAINLINK (LINK) 보유 시 현재 진행봉 0.9% + 다이버전스 듀얼 조건 (롱 + 숏)
    LINK 보유 시에만 실행, SOL 포지션 있으면 진입 금지
    ✅ 첫 매매 (SOL 0 개) → TP 걸기
    ✅ 추가 매수 (SOL > 0 개) → TP 안 걸기
    ✅ 현재봉 0.9% + 직전봉 다이버전스 (둘 다 만족)
    ✅ min_volatility, deviation, cond_price 모두 현재봉 현재가 기준
    ✅ 직전 15개 봉 close 기준 변동성 필터 추가 직전 15개봉 (고가-저가)/고가 > range_volatility_pct 2.3%
    """

    global last_sol_trade_time, last_sol_buy_time_1h, last_sol_buy_time_15m

    # SOL 포지션 체크: 있으면 진입 금지
    if has_position(MARKET_ID_SOL):
        print(f"[{symbol} LINK] SOL 포지션 있음으로 진입 금지")
        return

    # 쿨다운 체크 (60 초)
    if time.time() - last_sol_trade_time < 60:
        print(f"[{symbol} LINK] 60 초 쿨다운 중 진입 금지 (지난 체결 후 {time.time() - last_sol_trade_time:.1f}초 경과)")
        return

    # timeframe 별 쿨다운 체크
    if timeframe == '1h' and time.time() - last_sol_buy_time_1h < 3600:
        minutes_ago = (time.time() - last_sol_buy_time_1h) / 60
        print(f"[{symbol} LINK 1h] 최근 {minutes_ago:.1f}분 전에 1 시간봉 매수됨 (60 분 내 중복매수 금지)")
        return

    if timeframe == '15m' and time.time() - last_sol_buy_time_15m < 900:
        minutes_ago = (time.time() - last_sol_buy_time_15m) / 60
        print(f"[{symbol} LINK 15m] 최근 {minutes_ago:.1f}분 전에 15 분봉 매수됨 (15 분 내 중복매수 금지)")
        return

    set_margin_and_leverage(symbol)

    # CHAINLINK (LINK) 포지션 확인
    link_position = get_position_amount('LINK/USDT')
    if link_position == 0:
        print(f"[{symbol} LINK] CHAINLINK (LINK) 보유 없음 (진입 금지)")
        return

    print(f"[{symbol} LINK] LINK 보유량: {link_position}개")

    # 주문 수량 계산
    available_usdt = get_available_usdt()
    margin_to_use = available_usdt * 0.5
    current_price = float(exchange.fetch_ticker(symbol)['last'])
    notional = margin_to_use * LEVERAGE
    amount = round(notional / current_price, 3)

    if amount <= 0:
        print(f"[{symbol} LINK] 주문 수량이 0 이라서 중단")
        return

    # ──────────────────────────────────────────────────────────────
    # 1. 현재 진행봉 체크: 현재가 - 시가 차이 비율이 current_bar_pct (0.9%) 이상인지
    # ──────────────────────────────────────────────────────────────
    try:
        # 현재 진행봉 데이터 조회
        ohlcv_current = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=2)
        if ohlcv_current is None or len(ohlcv_current) < 2:
            print(f"[{symbol} LINK] 현재 진행봉 데이터 조회 실패")
            return

        current_bar_open = ohlcv_current[-1][1]  # open (시가)
        current_bar_close = current_price         # 현재가 (real-time)

        current_bar_change_pct = abs(current_bar_close - current_bar_open) / current_bar_open

        print(f"[{symbol} LINK] 현재 진행봉 변화율: {current_bar_change_pct*100:.2f}% (시가={current_bar_open:.6f}, 현재가={current_bar_close:.6f}, 기준: {current_bar_pct*100:.2f}%)")

        current_bar_cond = current_bar_change_pct >= current_bar_pct

        if not current_bar_cond:
            print(f"[{symbol} LINK] 현재 진행봉 변화율 {current_bar_change_pct*100:.2f}% 로 기준 {current_bar_pct*100:.2f}% 미만으로 진입 금지")
            return

        # ──────────────────────────────────────────────────────────────
        # 2. 현재봉 기준 min_volatility 체크 (현재가 vs 시가 변동률)
        # ──────────────────────────────────────────────────────────────
        current_volatility = abs(current_bar_close - current_bar_open) / current_bar_open
        vol_cond = current_volatility >= min_volatility

        print(f"[{symbol} LINK] 현재봉 변동성: {current_volatility*100:.2f}% (기준: {min_volatility*100:.2f}%)")

        if not vol_cond:
            print(f"[{symbol} LINK] 현재봉 변동성 {current_volatility*100:.2f}% 로 기준 {min_volatility*100:.2f}% 미만으로 진입 금지")
            return

    except Exception as e:
        print(f"[{symbol} LINK] 현재 진행봉 조회 실패: {e}")
        return

    # ──────────────────────────────────────────────────────────────
    # 3. 다이버전스 체크: 직전봉 (iloc[-1]) 기준으로 기존 다이버전스 로직
    # ──────────────────────────────────────────────────────────────
    df = get_confirmed_candles_with_rsi(symbol, timeframe)

    if len(df) < 18:
        print(f"[{symbol} LINK] 다이버전스 데이터 부족 (18 개 봉 필요)")
        return

    # 직전봉 (확정봉 중 마지막) = iloc[-1]
    prev_candle = df.iloc[-1]
    # 이전 15 개 봉 = iloc[-2:-17] (직전봉 제외)
    base_15 = df.iloc[-2:-17]

    if len(base_15) < 15:
        print(f"[{symbol} LINK] 직전 15개 봉 데이터 부족")
        return

    # 직전 15개 봉 close 기준 변동성 체크
    range_high = base_15['close'].max()
    range_low = base_15['close'].min()
    range_volatility = (range_high - range_low) / range_high

    print(f"[{symbol} LINK] 직전 15개 봉 close 변동성: {range_volatility*100:.2f}% (기준: {range_volatility_pct*100:.2f}%)")

    if range_volatility <= range_volatility_pct:
        print(f"[{symbol} LINK] 직전 15개 봉 변동성 미만으로 진입 금지")
        return

    # 상승 다이버전스 (롱)
    lowest_close = base_15['close'].min()
    lowest_rsi = base_15['rsi'].min()

    # 현재봉의 현재가 기준으로 비교 (prev_candle['close'] 대신 current_price 사용)
    cond_price_bull = current_price < lowest_close * (1 - price_diff_pct)
    cond_rsi_bull = prev_candle['rsi'] >= lowest_rsi * (1 + rsi_raise_pct)
    # vol_cond 는 이미 현재봉 기준으로 체크했다

    bull_signal = cond_price_bull and cond_rsi_bull and vol_cond

    # 하락 다이버전스 (숏)
    highest_close = base_15['close'].max()
    highest_rsi = base_15['rsi'].max()

    # 현재봉의 현재가 기준으로 비교
    cond_price_bear = current_price > highest_close * (1 + price_diff_pct)
    cond_rsi_bear = prev_candle['rsi'] <= highest_rsi * (1 - rsi_drop_pct)

    bear_signal = cond_price_bear and cond_rsi_bear and vol_cond

    print(f"[{symbol} LINK] BULL_SIGNAL={bull_signal} (price={cond_price_bull}, rsi={cond_rsi_bull}, vol={vol_cond})")
    print(f"[{symbol} LINK] BEAR_SIGNAL={bear_signal} (price={cond_price_bear}, rsi={cond_rsi_bear}, vol={vol_cond})")

    # ──────────────────────────────────────────────────────────────
    # 4. CME 편차 조건: 현재봉의 현재가 기준으로 체크
    # ──────────────────────────────────────────────────────────────
    try:
        cme_price = get_last_saturday_6_close()
    except Exception as e:
        print(f"[{symbol} LINK] 토요일 06:00 가격 조회 실패: {e}")
        return

    # 현재가 기준으로 CME 편차 체크
    deviation = abs(current_price - cme_price) / cme_price

    if deviation < 0.01:
        print(f"[{symbol} LINK] CME 편차 {deviation*100:.2f}% 미만으로 진입 금지 "
              f"| CME={cme_price:.2f}, current_price={current_price:.2f}")
        return

    print(f"[{symbol} LINK] CME 편차 {deviation*100:.2f}% 충족 "
          f"| CME={cme_price:.2f}, current_price={current_price:.2f}")

    # 현재 SOL 보유량 확인
    sol_position = get_position_amount('SOL/USDT')
    current_sol = sol_position if sol_position > 0 else 0

    # ──────────────────────────────────────────────────────────────
    # 듀얼 전략: 현재봉 0.9% + 다이버전스 (둘 다 만족)
    # ──────────────────────────────────────────────────────────────

    # 롱: 현재봉 상승 (>0.9%) + 상승 다이버전스
    if current_bar_cond and bull_signal:
        tp_price = current_price * (1 + tp_long_pct)
        exchange.create_market_buy_order(symbol, amount)

        last_sol_trade_time = time.time()
        if timeframe == '1h':
            last_sol_buy_time_1h = time.time()
        elif timeframe == '15m':
            last_sol_buy_time_15m = time.time()

        if current_sol == 0:
            place_tp_long(symbol, amount, tp_price)
            print(f"[{symbol} LINK] 듀얼 롱 진입 (현재봉 {current_bar_change_pct*100:.2f}% + 상승다이버, TP 걸림) | amount={amount} | price={current_price} | tp={tp_price}")
        else:
            print(f"[{symbol} LINK] 듀얼 롱 진입 (현재봉 {current_bar_change_pct*100:.2f}% + 상승다이버, TP 없음) | amount={amount} | price={current_price}")
        return

    # 숏: 현재봉 하락 (>0.9%) + 하락 다이버전스
    if current_bar_cond and bear_signal:
        tp_price = current_price * (1 - tp_short_pct)
        exchange.create_market_sell_order(symbol, amount)

        last_sol_trade_time = time.time()
        if timeframe == '1h':
            last_sol_buy_time_1h = time.time()
        elif timeframe == '15m':
            last_sol_buy_time_15m = time.time()

        if current_sol == 0:
            place_tp_short(symbol, amount, tp_price)
            print(f"[{symbol} LINK] 듀얼 숏 진입 (현재봉 {current_bar_change_pct*100:.2f}% + 하락다이버, TP 걸림) | amount={amount} | price={current_price} | tp={tp_price}")
        else:
            print(f"[{symbol} LINK] 듀얼 숏 진입 (현재봉 {current_bar_change_pct*100:.2f}% + 하락다이버, TP 없음) | amount={amount} | price={current_price}")
        return

    # 진입 조건 미충족
    if not bull_signal and not bear_signal:
        print(f"[{symbol} LINK] 다이버전스 미충족 (LONG={bull_signal}, SHORT={bear_signal})")
    elif current_bar_cond and not bull_signal and not bear_signal:
        print(f"[{symbol} LINK] 현재봉 조건 충족 but 다이버전스 없음")
    else:
        print(f"[{symbol} LINK] 진입 조건 없음")


# -------------------- 전역 변수 및 메인 루프 --------------------

last_run_date = None
last_sol_trade_time = 0  # 마지막 SOL 체결 시간 (60 초 쿨다운용)
last_sol_buy_time_1h = 0  # 마지막 SOL 1 시간봉 매수 시간 (60 분 쿨다운용)
last_sol_buy_time_15m = 0  # 마지막 SOL 15 분봉 매수 시간 (15 분 쿨다운용)

last_xrp_long_trade_time = 0
last_xrp_long_1h = 0
last_xrp_long_15m = 0

last_ada_short_trade_time = 0
last_ada_short_1h = 0
last_ada_short_15m = 0


while True:
    try:
        now = now_kst()

        # 09:00 KST SOL 기존 전략 (하루 1 회)
        if now.hour == 9 and now.minute == 0 and last_run_date != now.date():
            last_run_date = now.date()
            if not has_position(MARKET_ID_SOL):
                trade_once_sol()

        # 1시간봉 전략
        
        if not has_position(MARKET_ID_SOL):
            trade_rsi_strategy(
                symbol=SOL_SYMBOL,
                market_id=MARKET_ID_SOL,
                timeframe='1h',
                tp_long_pct=0.014, # 일반 익절률
                tp_long_pct_2=0.02, # 변동성 2% 이상 익절률
                tp_short_pct=0.01, 
                tp_short_pct_2=0.015, # 변동성 2% 이상 익절률
                min_volatility=0.0025,
                price_diff_pct=0.0005,
                min_range_volatility=0.01 #15봉 변동성 1% 미만시 진입 금지 
            )
            


        # 15분봉 전략
        if not has_position(MARKET_ID_SOL):
            trade_rsi_strategy(
                symbol=SOL_SYMBOL,
                market_id=MARKET_ID_SOL,
                timeframe='15m',
                tp_long_pct=0.014, # 일반 익절률
                tp_long_pct_2=0.02, # 변동성 2% 이상 익절률
                tp_short_pct=0.01, 
                tp_short_pct_2=0.015, # 변동성 2% 이상
                min_volatility=0.002,
                price_diff_pct=0.0005,  # ← 추가
                min_range_volatility=0.01   #15봉 변동성 1% 미만시 진입 금지             
            )


        # close 기준 RSI 다이버전스 전략 - 롱+숏 (SOL 1 시간봉)
        # rsi_raise_pct, rsi_drop_pct, price_diff_pct 모두 숫자 직접 입력
        if not has_position(MARKET_ID_SOL):
            trade_rsi_close_strategy(
                symbol=SOL_SYMBOL,
                market_id=MARKET_ID_SOL,
                timeframe='1h',
                tp_long_pct=0.014,
                tp_long_pct_2=0.02,
                tp_short_pct=0.01,
                tp_short_pct_2=0.015,
                min_volatility=0.0025,
                price_diff_pct=0.003,
                rsi_raise_pct=0.003, # 매수 제약룰이 있으니 평소횡보장일거란 말이지. 그러니깐 변동성이 작으니깐 rsi 작게 가져가자
                rsi_drop_pct=0.003 # 매수 제약룰이 있으니 평소횡보장일거란 말이지. 그러니깐 변동성이 작으니깐 rsi 작게 가져가자
            )


        # close 기준 RSI 다이버전스 전략 - 롱+숏 (SOL 15 분봉)
        if not has_position(MARKET_ID_SOL):
            trade_rsi_close_strategy(
                symbol=SOL_SYMBOL,
                market_id=MARKET_ID_SOL,
                timeframe='15m',
                tp_long_pct=0.014,
                tp_long_pct_2=0.02,
                tp_short_pct=0.01,
                tp_short_pct_2=0.015,
                min_volatility=0.0015,
                price_diff_pct=0.003, # 0.2% 로 바꾸면 노이즈 많이 낄려나?
                rsi_raise_pct=0.003, # 매수 제약룰이 있으니 평소횡보장일거란 말이지. 그러니깐 변동성이 작으니깐 작게 가져가자
                rsi_drop_pct=0.003  # 매수 제약룰이 있으니 평소횡보장일거란 말이지. 그러니깐 변동성이 작으니깐 rsi 작게 가져가자 0.3%
            )

        # ─────────────────────────────────────────
        # ★ 핵심: 기본 전략 후 2 초 대기
        # ─────────────────────────────────────────
        time.sleep(2)

        # XRP 보유 시 롱 전용
        xrp_position = get_position_amount('XRP/USDT')
        if xrp_position > 0:
            # 1 시간봉           
            trade_rsi_close_strategy_xrp_long(
                symbol=SOL_SYMBOL,
                market_id=MARKET_ID_SOL,
                timeframe='1h',
                tp_long_pct=0.012,
                tp_long_pct_2=0.02,
                min_volatility=0.0025,
                price_diff_pct=0.003,
                rsi_raise_pct=0.01,
                min_range_volatility=0.015         # 15봉 1.5% 변동성 없으면 무진입        
            )            
            # 15 분봉
            trade_rsi_close_strategy_xrp_long(
                symbol=SOL_SYMBOL,
                market_id=MARKET_ID_SOL,
                timeframe='15m',
                tp_long_pct=0.012,
                tp_long_pct_2=0.02,
                min_volatility=0.002,
                price_diff_pct=0.003,
                rsi_raise_pct=0.01,  # 매수 제약룰이 없고 하락장일거란 말이지. 그러니깐 변동성이 크니깐 rsi 제약 크게 가져가자 1%
                min_range_volatility=0.015   # 15봉 1.5% 변동성 없으면 무진입              
            )

        # ADA 보유 시 숏 전용
        ada_position = get_position_amount('ADA/USDT')
        if ada_position < 0:
            # 1 시간봉
            trade_rsi_close_strategy_ada_short(
                symbol=SOL_SYMBOL,
                market_id=MARKET_ID_SOL,
                timeframe='1h',
                tp_short_pct=0.012,
                tp_short_pct_2=0.02,
                min_volatility=0.0025,
                price_diff_pct=0.003,
                rsi_drop_pct=0.01,
                min_range_volatility=0.015                
            )
            # 15 분봉
            trade_rsi_close_strategy_ada_short(
                symbol=SOL_SYMBOL,
                market_id=MARKET_ID_SOL,
                timeframe='15m',
                tp_short_pct=0.012,
                tp_short_pct_2=0.02,
                min_volatility=0.002,                
                price_diff_pct=0.003,
                rsi_drop_pct=0.01,
                min_range_volatility=0.015                
            )

        # DOGE 보유 시 롱 + 숏 전용 (SOL 포지션 있으면 진입 금지)
        doge_position = get_position_amount('DOGE/USDT')
        if doge_position != 0 and not has_position(MARKET_ID_SOL): # DOGE 보유 시에만 실행 (보유량 0 이 아니면 모두 포함) # SOL 체크 추가    
            # 1 시간봉
            trade_rsi_close_strategy_doge(
                symbol=SOL_SYMBOL,
                market_id=MARKET_ID_SOL,
                timeframe='1h',
                tp_long_pct=0.02,
                tp_short_pct=0.015,
                min_volatility=0.0025,
                price_diff_pct=0.001, #close 가격 0.1% 차이
                rsi_raise_pct=0.003, # rsi  0.3% 차이
                rsi_drop_pct=0.003
            )
            # 15 분봉
            trade_rsi_close_strategy_doge(
                symbol=SOL_SYMBOL,
                market_id=MARKET_ID_SOL,
                timeframe='15m',
                tp_long_pct=0.02,
                tp_short_pct=0.015,
                min_volatility=0.002,
                price_diff_pct=0.001,
                rsi_raise_pct=0.003,
                rsi_drop_pct=0.003
            )


        # ──────────────────────────────────────────────────────────────
        # CHAINLINK (LINK) 보유 시 현재봉 0.9% 변동성 + 다이버전스 듀얼 전략 (롱 + 숏)
        # ──────────────────────────────────────────────────────────────
        
        
        link_position = get_position_amount('LINK/USDT')
        if link_position != 0 and not has_position(MARKET_ID_SOL):
            print(f"[LINK] LINK 보유량: {link_position}개 - 0.9%+다이버전스 듀얼 전략 실행")
            
          
            # 1 시간봉
            trade_current_bar_09_pct_strategy(
                symbol=SOL_SYMBOL,
                market_id=MARKET_ID_SOL,
                timeframe='1h',
                tp_long_pct=0.015,     # 롱 익절 %도 보수적으로
                tp_short_pct=0.01,   # 숏시 익절 % 보수적으로가자
                min_volatility=0.0025, # 이미 현재봉이 -0.9%일테니 변동성은 의미없음
                current_bar_pct=0.01, # 현재봉이 시가대비 -1% 하락시 조건 발동 (1h 봉)
                price_diff_pct=0.004, # 현재봉이 그래도 직전 15개봉들의 lowest close보다 0.4%는 낮아야지 (1h 봉)
                rsi_raise_pct=0.02, # 직전봉의 rsi를 보기 때문에 2% 높게 설정
                rsi_drop_pct=0.02,  # 직전봉의 rsi를 보기 때문에 2% 높게 설정
                range_volatility_pct=0.023 # 직전 15봉의 (고가-저가)/고가 > 2.3% 이상 변동성 필요              
            )
            # 15 분봉
            trade_current_bar_09_pct_strategy(
                symbol=SOL_SYMBOL,
                market_id=MARKET_ID_SOL,
                timeframe='15m',
                tp_long_pct=0.015,
                tp_short_pct=0.01,
                min_volatility=0.0025,
                current_bar_pct=0.008,
                price_diff_pct=0.003,
                rsi_raise_pct=0.02,  # 직전봉의 rsi를 보기 때문에 2% 높게 설정
                rsi_drop_pct=0.02,   # 직전봉의 rsi를 보기 때문에 2% 높게 설정
                range_volatility_pct=0.023                
            )

        time.sleep(23)  # 25 초 간격

    except Exception as e:
        print(f"[MAIN ERROR] {e}")
        time.sleep(3)