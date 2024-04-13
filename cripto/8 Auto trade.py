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

def get_target_price(ticker):
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[1]['low']
    return target_price

def get_target_priceE(ticker):
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_priceE = df.iloc[1]['low']
    return target_priceE

def get_target_priceX(ticker):
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_priceX = df.iloc[1]['low']
    return target_priceX

def get_target_priceA(ticker):
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_priceA = df.iloc[1]['low']
    return target_priceA     
    

def get_target_pricebch(ticker):
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_pricebch = df.iloc[1]['low']
    return target_pricebch   

def get_target_priceltc(ticker):
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_priceltc = df.iloc[1]['low']
    return target_priceltc

def get_target_pricexlm(ticker):
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_pricexlm = df.iloc[1]['low']
    return target_pricexlm         

def get_target_priceeos(ticker):
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_priceeos = df.iloc[1]['low']
    return target_priceeos           

def get_ma10(ticker):
    """10일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=10)
    ma10 = df['close'].rolling(10).mean().iloc[-1]
    return ma10    


def get_ma10E(ticker):
    """10일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=10)
    ma10E = df['close'].rolling(10).mean().iloc[-1]
    return ma10E        

def get_ma10X(ticker):
    """10일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=10)
    ma10X = df['close'].rolling(10).mean().iloc[-1]
    return ma10X      
     

def get_ma10A(ticker):
    """10일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=10)
    ma10A = df['close'].rolling(10).mean().iloc[-1]
    return ma10A    
   
def get_ma10bch(ticker):
    """10일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=10)
    ma10bch = df['close'].rolling(10).mean().iloc[-1]
    return ma10bch

def get_ma10ltc(ticker):
    """10일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=10)
    ma10ltc = df['close'].rolling(10).mean().iloc[-1]
    return ma10ltc           

def get_ma10xlm(ticker):
    """10일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=10)
    ma10xlm = df['close'].rolling(10).mean().iloc[-1]
    return ma10xlm    


def get_ma10eos(ticker):
    """10일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=10)
    ma10eos = df['close'].rolling(10).mean().iloc[-1]
    return ma10eos     


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

def get_current_priceX(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"] 

def get_current_priceA(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"] 

def get_current_priceL(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"] 

def get_current_pricebch(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

def get_current_priceltc(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

def get_current_pricexlm(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

def get_current_priceeos(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]


# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
# 시작 메세지 슬랙 전송
post_message(myToken,"#crypto", "autotrade start")


while True:
    try:
        current_price = get_current_price("KRW-BTC")
        target_price = get_target_price("KRW-BTC")
        ma10 = get_ma10("KRW-BTC")

        current_priceE = get_current_priceE("KRW-ETH") 
        target_priceE = get_target_priceE("KRW-ETH")
        ma10E = get_ma10E("KRW-ETH")       


        current_priceX = get_current_priceX("KRW-XRP") 
        target_priceX = get_target_priceX("KRW-XRP")
        ma10X = get_ma10X("KRW-XRP")

        current_priceA = get_current_priceA("KRW-ADA")
        target_priceA = get_target_priceA("KRW-ADA")
        ma10A = get_ma10A("KRW-ADA")

        current_pricebch = get_current_pricebch("KRW-BCH")
        target_pricebch = get_target_pricebch("KRW-BCH")
        ma10bch = get_ma10bch("KRW-BCH")


        current_priceltc = get_current_priceltc("KRW-LTC")
        target_priceltc = get_target_priceltc("KRW-LTC")
        ma10ltc = get_ma10ltc("KRW-LTC")          


        current_pricexlm = get_current_pricexlm("KRW-XLM")
        target_pricexlm = get_target_pricexlm("KRW-XLM")
        ma10xlm = get_ma10xlm("KRW-XLM")


        current_priceeos = get_current_priceeos("KRW-EOS")
        target_priceeos = get_target_priceeos("KRW-EOS")
        ma10eos = get_ma10eos("KRW-EOS")
      


        if ma10 < target_price :

            if ma10*1.03 < current_price :
                krw = get_balance("KRW")
                btc = get_balance("BTC")
                if btc < 0.0001:
                    buy_result = upbit.buy_market_order("KRW-BTC", krw*(0.1))            

            elif ma10 < current_price :
                krw = get_balance("KRW")
                btc = get_balance("BTC")
                if btc < 0.0001:
                    buy_result = upbit.buy_market_order("KRW-BTC", krw*(0.2))

        else:
            btc = get_balance("BTC")
            if btc > 0.00004:
                sell_result = upbit.sell_market_order("KRW-BTC", btc)



        if ma10E < target_priceE :

            if ma10E*1.03 < current_priceE :
                krw = get_balance("KRW")
                eth = get_balance("ETH")
                if eth < 0.0001:
                    buy_result = upbit.buy_market_order("KRW-ETH", krw*(0.1))            

            elif ma10E < current_priceE :
                krw = get_balance("KRW")
                eth = get_balance("ETH")
                if eth < 0.0001:
                    buy_result = upbit.buy_market_order("KRW-ETH", krw*(0.2))

        else:
            eth = get_balance("ETH")
            if eth > 0.00004:
                sell_result = upbit.sell_market_order("KRW-ETH", eth)     



        if ma10X < target_priceX :

            if ma10X*1.03 < current_priceX :
                krw = get_balance("KRW")
                xrp = get_balance("XRP")
                if xrp < 0.01:
                    buy_result = upbit.buy_market_order("KRW-XRP", krw*(0.1))

            elif ma10X < current_priceX :
                krw = get_balance("KRW")
                xrp = get_balance("XRP")
                if xrp < 0.01:
                    buy_result = upbit.buy_market_order("KRW-XRP", krw*(0.2))

        else:               
            xrp = get_balance("XRP")
            if xrp > 0.001:
                sell_result = upbit.sell_market_order("KRW-XRP", xrp)


        if ma10A < target_priceA :

            if ma10A*1.03 < current_priceA :    
                krw = get_balance("KRW")
                ada = get_balance("ADA")
                if ada < 0.01:
                    buy_result = upbit.buy_market_order("KRW-ADA", krw*(0.1))

            elif ma10A < current_priceA :    
                krw = get_balance("KRW")
                ada = get_balance("ADA")
                if ada < 0.01:
                    buy_result = upbit.buy_market_order("KRW-ADA", krw*(0.2))

        else:               
            ada = get_balance("ADA")
            if ada > 0.001:
                sell_result = upbit.sell_market_order("KRW-ADA", ada)


        if ma10bch < target_pricebch :

            if ma10bch*1.03 < current_pricebch :
                krw = get_balance("KRW")
                bch = get_balance("BCH")
                if bch < 0.1:
                    buy_result = upbit.buy_market_order("KRW-BCH", krw*(0.05))            

            elif ma10bch < current_pricebch :
                krw = get_balance("KRW")
                bch = get_balance("BCH")
                if bch < 0.1:
                    buy_result = upbit.buy_market_order("KRW-BCH", krw*(0.1))

        else:
            bch = get_balance("BCH")
            if bch > 0.04:
                sell_result = upbit.sell_market_order("KRW-BCH", bch)



        if ma10ltc < target_priceltc :

            if ma10ltc*1.03 < current_priceltc :
                krw = get_balance("KRW")
                ltc = get_balance("LTC")
                if ltc < 0.01:                    
                    buy_result = upbit.buy_market_order("KRW-LTC", krw*(0.05))           

            elif ma10ltc < current_priceltc :
                krw = get_balance("KRW")
                ltc = get_balance("LTC")
                if ltc < 0.01:                    
                    buy_result = upbit.buy_market_order("KRW-LTC", krw*(0.1))

        else:
            ltc = get_balance("LTC")
            if ltc > 0.004:
                sell_result = upbit.sell_market_order("KRW-LTC", ltc)

                
        time.sleep(1)
    except Exception as e:
        print(e)
        post_message(myToken,"#crypto", e)
        time.sleep(1)