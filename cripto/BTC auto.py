import time
import pyupbit
import datetime

access = "AUxribSOSKLzHl4WOM8SYCdx6fCiQB9rlfyxh2oU"
secret = "8BeMmarN0EgF1QoUBPLK9dxKW8PVoDFd8M6ZLxeU"

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price


def get_open_price(ticker):
    """09:00 시작가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    open_price = df.iloc[0]['close']
    return open_price  

def get_target_percent(ticker):
    """변동성 돌파 전략에 전날 변동성 계산"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_percent = (df.iloc[0]['high'] - df.iloc[0]['low'])/df.iloc[0]['close']
    return target_percent        

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_ma5(ticker):
    """5일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    ma5 = df['close'].rolling(5).mean().iloc[-1]
    return ma5

def get_ma20(ticker):
    """20일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=20)
    ma20 = df['close'].rolling(20).mean().iloc[-1]
    return ma20 

def get_ma30(ticker):
    """30일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=30)
    ma30 = df['close'].rolling(30).mean().iloc[-1]
    return ma30      

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(hours=24) - datetime.timedelta(minutes=2)

        open_price = get_open_price("KRW-BTC")
        current_price = get_current_price("KRW-BTC")
        target_price = get_target_price("KRW-BTC", 0.3)
        ma5 = get_ma5("KRW-BTC")
        ma20 = get_ma20("KRW-BTC")
        ma30 = get_ma30("KRW-BTC")        
        target_percent = get_target_percent("KRW-BTC")*100 

        if start_time < now < end_time or open_price*0.996 > current_price :

            if target_price <= current_price and ma5 <= current_price and ma20 <= current_price and ma30 <= current_price:
                krw = get_balance("KRW")
                btc = get_balance("BTC")
                if target_percent  <= 0.02:
                    if btc < 0.001:
                        buy_result = upbit.buy_market_order("KRW-BTC", krw*(0.999))
                elif 0.02 < target_percent:
                    if btc < 0.001:
                        buy_result = upbit.buy_market_order("KRW-BTC", krw*(2/target_percent))                  

        else:
            btc = get_balance("BTC")
            if btc > 0.0005:
                sell_result = upbit.sell_market_order("KRW-BTC", btc)

        time.sleep(5)
    except Exception as e:
        print(e)
        time.sleep(1)