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

def get_target_priceE(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_priceE = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_priceE

def get_open_price(ticker):
    """09:00 시작가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    open_price = df.iloc[0]['close']
    return open_price  

def get_open_priceE(ticker):
    """09:00 시작가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    open_priceE = df.iloc[0]['close']
    return open_priceE      

def get_target_percent(ticker):
    """변동성 돌파 전략에 전날 변동성 계산"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_percent = (df.iloc[0]['high'] - df.iloc[0]['low'])/df.iloc[0]['close']
    return target_percent     

def get_target_percentE(ticker):
    """변동성 돌파 전략에 전날 변동성 계산"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_percentE = (df.iloc[0]['high'] - df.iloc[0]['low'])/df.iloc[0]['close']
    return target_percentE        

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_ma5(ticker):
    """5일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=6)
    ma5 = df['close'].rolling(5).mean().iloc[-2]
    return ma5

def get_ma5E(ticker):
    """5일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=6)
    ma5E = df['close'].rolling(5).mean().iloc[-2]
    return ma5E    

def get_ma20(ticker):
    """20일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=21)
    ma20 = df['close'].rolling(20).mean().iloc[-2]
    return ma20 

def get_ma20E(ticker):
    """20일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=21)
    ma20E = df['close'].rolling(20).mean().iloc[-2]
    return ma20E    

def get_ma30(ticker):
    """30일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=31)
    ma30 = df['close'].rolling(30).mean().iloc[-2]
    return ma30   

def get_ma30E(ticker):
    """30일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=31)
    ma30E = df['close'].rolling(30).mean().iloc[-2]
    return ma30E         
    

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

def get_current_priceE(ticker):
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

        open_priceE = get_open_priceE("KRW-ETH")
        current_priceE = get_current_priceE("KRW-ETH")
        target_priceE = get_target_priceE("KRW-ETH", 0.3)
        ma5E = get_ma5E("KRW-ETH")
        ma20E = get_ma20E("KRW-ETH")
        ma30E = get_ma30E("KRW-ETH")        
        target_percentE = get_target_percentE("KRW-ETH")*100 
        
        krw = get_balance("KRW")
        btc = get_balance("BTC")
        eth = get_balance("ETH")

        if start_time < now < end_time or open_price*0.996 > current_price :

            if target_price <= current_price and ma5 <= current_price and ma20 <= current_price and ma30 <= current_price:

                if eth > 0.01:
                    if target_percent  <= 0.02:
                        if btc < 0.001:
                            buy_result = upbit.buy_market_order("KRW-BTC", krw*(0.999))
                    elif 0.02 < target_percent:
                        if btc < 0.001:
                            buy_result = upbit.buy_market_order("KRW-BTC", krw*(2/target_percent))                  


                if eth < 0.01:
                    if target_percent  <= 0.02:
                        if btc < 0.001:
                            buy_result = upbit.buy_market_order("KRW-BTC", krw*(0.499))
                    elif 0.02 < target_percent:
                        if btc < 0.001:
                            buy_result = upbit.buy_market_order("KRW-BTC", krw*(1/target_percent)) 
        else:
            btc = get_balance("BTC")
            if btc > 0.0005:
                sell_result = upbit.sell_market_order("KRW-BTC", btc)

        if start_time < now < end_time or open_priceE*0.996 > current_priceE :

            if target_priceE <= current_priceE and ma5E <= current_priceE and ma20E <= current_priceE and ma30E <= current_priceE:

                if btc > 0.001:
                    if target_percentE  <= 0.02:
                        if eth < 0.001:
                            buy_result = upbit.buy_market_order("KRW-ETH", krw*(0.999))
                    elif 0.02 < target_percentE:
                        if eth < 0.001:
                            buy_result = upbit.buy_market_order("KRW-ETH", krw*(2/target_percentE))                  


                if btc < 0.001:
                    if target_percentE  <= 0.02:
                        if eth < 0.001:
                            buy_result = upbit.buy_market_order("KRW-ETH", krw*(0.499))
                    elif 0.02 < target_percentE:
                        if eth < 0.001:
                            buy_result = upbit.buy_market_order("KRW-ETH", krw*(1/target_percentE)) 
        else:
            btc = get_balance("ETH")
            if eth > 0.005:
                sell_result = upbit.sell_market_order("KRW-ETH", eth)


        time.sleep(5)
    except Exception as e:
        print(e)
        time.sleep(1)



