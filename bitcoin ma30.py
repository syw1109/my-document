import time
import pyupbit
import datetime

access = "AUxribSOSKLzHl4WOM8SYCdx6fCiQB9rlfyxh2oU"
secret = "8BeMmarN0EgF1QoUBPLK9dxKW8PVoDFd8M6ZLxeU"

def get_close_price(ticker):
    """30 돌파 전략으로 매수 목표가 조회"""
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    close_price = df.iloc[1]['close']
    return close_price

def get_Ref_price(ticker):
    """30 돌파 전략으로 매수 목표가 조회"""
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    Ref_price = df.iloc[0]['close']
    return Ref_price
 

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_ma30(ticker):
    """30일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=30)
    ma30 = df['close'].rolling(30).mean().iloc[0]
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


def get_Ref_price(ticker):
    """30 돌파 전략으로 매수 목표가 조회"""
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    Ref_price = df.iloc[0]['close']
    return Ref_price    

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
        end_time = start_time + datetime.timedelta(hours=24)
        current_price = get_current_price("KRW-BTC")
        close_price = get_close_price("KRW-BTC")
        Ref_price = get_Ref_price("KRW-BTC")
        ma30 = get_ma30("KRW-BTC")
        krw = get_balance("KRW")
        btc = get_balance("BTC")

        if  ma30 < current_price:
            if Ref_price < close_price :                
                if krw  > 1001000:
                    buy_result = upbit.buy_market_order("KRW-BTC", 1000000)
                                     

        else:
            btc = get_balance("BTC")
            if btc > 0.00004:
                sell_result = upbit.sell_market_order("KRW-BTC", btc)

                                                                 
                
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)        