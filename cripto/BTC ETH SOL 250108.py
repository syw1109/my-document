# GPT한테 간결화 해달라고 했는데 머가 좀 빠진듯
import time
import pyupbit
import datetime

# API 키 설정
access = "VjbtLbzbFoAVeILkHwCC4PFc5l8lcfQJghzBVBmD"
secret = "gL8xagr10FdayU7dWjtI5XZ1pwratIbe9xjy9Jc9"
upbit = pyupbit.Upbit(access, secret)

def get_ohlcv(ticker, interval="day", count=2):
    return pyupbit.get_ohlcv(ticker, interval=interval, count=count)

def get_ma(ticker, period, column='close', count=None):
    df = get_ohlcv(ticker, count=count or period+1)
    if column == 'hykin':
        df['hykin'] = (df['high'] + df['low'] + df['open'] + df['close']) / 4
    return df[column if column != 'hykin' else 'hykin'].rolling(period).mean().iloc[-2]

def get_balance(ticker):
    balances = upbit.get_balances()
    return next((float(b['balance']) for b in balances if b['currency'] == ticker), 0)

def get_current_price(ticker):
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

def buy_crypto(ticker, ratio):
    krw = get_balance("KRW")
    upbit.buy_market_order(ticker, krw * ratio)

def sell_crypto(ticker):
    balance = get_balance(ticker.split('-')[1])
    if balance > 0:
        upbit.sell_market_order(ticker, balance)

def check_conditions(ticker, ma_periods, thresholds, columns):
    df = get_ohlcv(ticker)
    open_price, low_price = df.iloc[0]['close'], df.iloc[1]['low']
    ma_values = [get_ma(ticker, period, column) for period, column in zip(ma_periods, columns)]
    
    conditions = [
        all(open_price < ma * thresh[0] for ma, thresh in zip(ma_values, thresholds)),
        all(low_price > ma * thresh[1] for ma, thresh in zip(ma_values, thresholds)),
        all(open_price > ma * thresh[2] for ma, thresh in zip(ma_values, thresholds))
    ]
    return all(conditions)

print("autotrade start")

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_ohlcv("KRW-BTC").index[0]
        end_time = start_time + datetime.timedelta(minutes=1)

        if now > end_time:
            btc = get_balance("BTC")
            eth = get_balance("ETH")
            sol = get_balance("SOL")

            # BTC 조건 확인 및 거래
            if check_conditions("KRW-BTC", [31, 45], [(1.02, 0.98, 0.997), (1.02, 0.98, 1)], ['hykin', 'hykin']):
                if btc < 0.0005:
                    buy_ratio = 0.4 if eth < 0.01 and sol < 0.05 else 0.57 if (eth > 0.01) ^ (sol > 0.05) else 0.999
                    buy_crypto("KRW-BTC", buy_ratio)
            elif btc > 0.0005:
                sell_crypto("KRW-BTC")

            # ETH 조건 확인 및 거래
            if check_conditions("KRW-ETH", [20, 30], [(1.025, 0.975, 0.997), (1.025, 0.975, 1)], ['close', 'close']):
                if eth < 0.001:
                    buy_ratio = 0.3 if btc < 0.001 and sol < 0.05 else 0.43 if (btc > 0.001) ^ (sol > 0.05) else 0.999
                    buy_crypto("KRW-ETH", buy_ratio)
            elif eth > 0.01:
                sell_crypto("KRW-ETH")

            # SOL 조건 확인 및 거래
            if check_conditions("KRW-SOL", [16, 44], [(1.07, 0.98, 1), (1.07, 1, 1)], ['high', 'close']):
                if sol < 0.1:
                    buy_ratio = 0.3 if eth < 0.1 and btc < 0.001 else 0.43 if (eth > 0.1) ^ (btc > 0.001) else 0.999
                    buy_crypto("KRW-SOL", buy_ratio)
            elif sol > 0.05:
                sell_crypto("KRW-SOL")

        time.sleep(20)
    except Exception as e:
        print(e)
        time.sleep(10)
