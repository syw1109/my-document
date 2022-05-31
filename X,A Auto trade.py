import time
import pyupbit
import datetime
import requests

access = "AUxribSOSKLzHl4WOM8SYCdx6fCiQB9rlfyxh2oU"
secret = "8BeMmarN0EgF1QoUBPLK9dxKW8PVoDFd8M6ZLxeU"
myToken = "xoxb-your-token"

def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )



def get_target_priceX(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_priceX = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_priceX

def get_target_priceA(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_priceA = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_priceA     
                   
  



def get_open_priceX(ticker):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    open_priceX = df.iloc[0]['close']
    return open_priceX  

def get_open_priceA(ticker):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    open_priceA = df.iloc[0]['close']
    return open_priceA     
 
          





def get_target_percentX(ticker):
    """변동성 돌파 전략에 전날 변동성 계산"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_percentX = (df.iloc[0]['high'] - df.iloc[0]['low'])/df.iloc[0]['close'] 
    return target_percentX  

def get_target_percentA(ticker):
    """변동성 돌파 전략에 전날 변동성 계산"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_percentA = (df.iloc[0]['high'] - df.iloc[0]['low'])/df.iloc[0]['close'] 
    return target_percentA 
 




def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    start_time = df.index[0]
    return start_time



def get_ma5X(ticker):
    """5일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    ma5X = df['close'].rolling(5).mean().iloc[-1]
    return ma5X

def get_ma10X(ticker):
    """10일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=10)
    ma10X = df['close'].rolling(10).mean().iloc[-1]
    return ma10X      

def get_ma20X(ticker):
    """20일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=20)
    ma20X = df['close'].rolling(20).mean().iloc[-1]
    return ma20X         

def get_ma5A(ticker):
    """5일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    ma5A = df['close'].rolling(5).mean().iloc[-1]
    return ma5A  

def get_ma10A(ticker):
    """10일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=10)
    ma10A = df['close'].rolling(10).mean().iloc[-1]
    return ma10A 
   



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


def get_current_priceX(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"] 

def get_current_priceA(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"] 



# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
# 시작 메세지 슬랙 전송
post_message(myToken,"#crypto", "autotrade start")


while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(hours=24)


        open_priceX = get_open_priceX("KRW-XRP")
        current_priceX = get_current_priceX("KRW-XRP") 
        target_priceX = get_target_priceX("KRW-XRP", 0.5)
        ma5X = get_ma5X("KRW-XRP")
        ma10X = get_ma10X("KRW-XRP")
        ma20X = get_ma20X("KRW-XRP")
        target_percentX = get_target_percentX("KRW-XRP")

        open_priceA = get_open_priceA("KRW-ADA")
        current_priceA = get_current_priceA("KRW-ADA")
        target_priceA = get_target_priceA("KRW-ADA", 0.3)
        ma5A = get_ma5A("KRW-ADA")
        ma10A = get_ma10A("KRW-ADA")
        target_percentA = get_target_percentA("KRW-ADA")
     

                         
                                 
        if start_time < now < end_time - datetime.timedelta(minutes=10) :
            if target_priceX < current_priceX and ma5X < current_priceX and ma10X < current_priceX:
                krw = get_balance("KRW")
                xrp = get_balance("XRP")
                if target_percentX  <= 0.015:
                    if xrp < 0.01:
                        buy_result = upbit.buy_market_order("KRW-XRP", krw*(0.3))

                elif 0.015 < target_percentX:
                    if xrp < 0.01:
                        buy_result = upbit.buy_market_order("KRW-XRP", krw*(1/target_percentX/300))


        else:               
            xrp = get_balance("XRP")
            if xrp > 0.001:
                sell_result = upbit.sell_market_order("KRW-XRP", xrp)


        if start_time < now < end_time - datetime.timedelta(minutes=10) : 
            if target_priceA < current_priceA and ma5A < current_priceA and ma10A < current_priceA:
                krw = get_balance("KRW")
                ada = get_balance("ADA")
                if target_percentA  <= 0.015:
                    if ada < 0.01:
                        buy_result = upbit.buy_market_order("KRW-ADA", krw*(0.3))

                elif 0.015 < target_percentA:
                    if ada < 0.01:
                        buy_result = upbit.buy_market_order("KRW-ADA", krw*(1/target_percentA/300))

        else:               
            ada = get_balance("ADA")
            if ada > 0.001:
                sell_result = upbit.sell_market_order("KRW-ADA", ada)
                                  


                
        time.sleep(1)
    except Exception as e:
        print(e)
        post_message(myToken,"#crypto", e)
        time.sleep(1)