
# 바이낸스 SOL/USDT 선물.
# 격리(Isolated) 마진.
# 레버리지 5배.
# 선물계좌 증거금의 50% 사용.
# 기존 SOL 포지션이 있으면 거래 안 함.
# 금요일/토요일 매매 금지.
# 현재가와 토요일 기준가 차이가 ±9% 이상이면 거래 금지.
# 업비트 SOL 18일 MA가 5일 연속 상승이면 숏 금지.
# 업비트 SOL 18일 MA가 5일 연속 하락이면 롱 금지.
# 업비트 SOL 오늘 시가가 18일/43일 이평선보다 높으면 숏 금지.
# 수요일/목요일은 TP 1% 적용, 그 외는 토요일 기준가 TP.

# while문X 바로 테스트 용

import time
import datetime
import ccxt
import pyupbit
import pandas as pd
from datetime import timezone, timedelta

KST = timezone(timedelta(hours=9))
SYMBOL = 'SOL/USDT'
UPBIT_TICKER = 'KRW-SOL'
MARKET_ID = 'SOLUSDT'
LEVERAGE = 5

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
    return datetime.datetime.now(KST)

def get_last_saturday_6_close():
    now = now_kst()
    sat6 = now.replace(hour=6, minute=0, second=0, microsecond=0)
    while sat6.weekday() != 5:
        sat6 -= datetime.timedelta(days=1)
    if now < sat6:
        sat6 -= datetime.timedelta(days=7)

    since_ms = int((sat6 - datetime.timedelta(days=7)).timestamp() * 1000)
    klines = exchange.fetch_ohlcv(SYMBOL, timeframe='1h', since=since_ms, limit=200)
    target_ms = int(sat6.astimezone(datetime.timezone.utc).timestamp() * 1000)

    for o in klines:
        if o[0] == target_ms:
            return float(o[4])
    raise ValueError("토요일 06:00 종가를 찾지 못했습니다.")

def has_sol_position():
    balance = exchange.fetch_balance(params={'type': 'future'})
    positions = balance.get('info', {}).get('positions', [])
    for p in positions:
        if p.get('symbol') == MARKET_ID and abs(float(p.get('positionAmt', 0))) > 0:
            return True
    return False

def get_available_usdt():
    balance = exchange.fetch_balance(params={'type': 'future'})
    return float(balance.get('free', {}).get('USDT', 0))

def set_margin_and_leverage():
    exchange.load_markets()
    exchange.set_margin_mode('isolated', SYMBOL)
    exchange.set_leverage(LEVERAGE, SYMBOL)

def place_tp_long(qty, tp_price):
    exchange.create_order(
        symbol=SYMBOL,
        type='TAKE_PROFIT_MARKET',
        side='sell',
        amount=qty,
        params={
            'stopPrice': tp_price,
            'closePosition': True,
            'workingType': 'MARK_PRICE'
        }
    )

def place_tp_short(qty, tp_price):
    exchange.create_order(
        symbol=SYMBOL,
        type='TAKE_PROFIT_MARKET',
        side='buy',
        amount=qty,
        params={
            'stopPrice': tp_price,
            'closePosition': True,
            'workingType': 'MARK_PRICE'
        }
    )

def get_upbit_ma18_ma43():
    df = pyupbit.get_ohlcv(UPBIT_TICKER, interval="day", count=60)
    if df is None or len(df) < 43:
        raise ValueError("업비트 일봉 데이터가 부족합니다.")
    df["ma18"] = df["close"].rolling(18).mean()
    df["ma43"] = df["close"].rolling(43).mean()
    last = df.dropna().iloc[-1]
    return float(last["ma18"]), float(last["ma43"])

def get_upbit_ma18_series():
    df = pyupbit.get_ohlcv(UPBIT_TICKER, interval="day", count=30)
    if df is None or len(df) < 18:
        raise ValueError("업비트 일봉 데이터가 부족합니다.")
    df["ma18"] = df["close"].rolling(18).mean()
    return df["ma18"].dropna()

def ma18_5day_trend():
    ma = get_upbit_ma18_series()
    last5 = ma.iloc[-5:].tolist()
    if len(last5) < 5:
        return None

    up = all(last5[i] > last5[i - 1] for i in range(1, 5))
    down = all(last5[i] < last5[i - 1] for i in range(1, 5))

    return {
        "up_5days": up,
        "down_5days": down,
        "last_ma18": last5[-1]
    }

def get_upbit_today_open():
    df = pyupbit.get_ohlcv(UPBIT_TICKER, interval="day", count=2)
    if df is None or len(df) < 1:
        raise ValueError("업비트 오픈가 데이터를 가져오지 못했습니다.")
    return float(df.iloc[-1]["open"])

def trade_once():
    set_margin_and_leverage()

    now = now_kst()
    if now.weekday() in [4, 5]:
        print("금요일/토요일은 매매 금지")
        return

    if has_sol_position():
        print("기존 SOL 포지션이 있어서 거래하지 않음")
        return

    sat_close = get_last_saturday_6_close()
    current_price = float(exchange.fetch_ticker(SYMBOL)['last'])

    if current_price <= sat_close * 0.91 or current_price >= sat_close * 1.09:
        print("현재가와 토요일 기준가가 9% 이상 차이 나서 매매 금지")
        return

    trend = ma18_5day_trend()
    if trend is None:
        print("MA18 추세 데이터를 가져오지 못했습니다.")
        return

    upbit_ma18, upbit_ma43 = get_upbit_ma18_ma43()
    upbit_today_open = get_upbit_today_open()

    available_usdt = get_available_usdt()
    margin_to_use = available_usdt * 0.5
    notional = margin_to_use * LEVERAGE
    amount = round(notional / current_price, 3)

    if amount <= 0:
        print("주문 수량이 0이라서 중단")
        return

    weekday = now.weekday()
    tp_price_long = current_price * 1.01 if weekday in [2, 3] else sat_close
    tp_price_short = current_price * 0.99 if weekday in [2, 3] else sat_close

    if current_price <= sat_close * 0.99:
        if trend["down_5days"]:
            print("5일 연속 하락이라 롱 진입 금지")
            return

        exchange.create_market_buy_order(SYMBOL, amount)
        place_tp_long(amount, tp_price_long)
        print(f"롱 진입 | amount={amount} | price={current_price} | tp={tp_price_long}")

    elif current_price >= sat_close * 1.01:
        if trend["up_5days"]:
            print("5일 연속 상승이라 숏 진입 금지")
            return

        if upbit_today_open > upbit_ma18 and upbit_today_open > upbit_ma43:
            print("업비트 오늘 오픈가가 18일/43일 이평선보다 높아서 숏 진입 금지")
            return

        exchange.create_market_sell_order(SYMBOL, amount)
        place_tp_short(amount, tp_price_short)
        print(f"숏 진입 | amount={amount} | price={current_price} | tp={tp_price_short}")

    else:
        print("진입 조건 없음")

try:
    trade_once()
except Exception as e:
    print(e)
