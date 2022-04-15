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

def get_target_priceEC(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_priceEC = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_priceEC       

def get_target_priceL(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_priceL = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_priceL            
  
def get_open_price(ticker):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    open_price = df.iloc[0]['close']
    return open_price  

def get_open_priceE(ticker):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    open_priceE = df.iloc[0]['close']
    return open_priceE   

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

def get_open_priceEC(ticker):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    open_priceEC = df.iloc[0]['close']
    return open_priceEC

def get_open_priceL(ticker):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    open_priceL = df.iloc[0]['close']
    return open_priceL                 

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

def get_target_percentEC(ticker):
    """변동성 돌파 전략에 전날 변동성 계산"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_percentEC = (df.iloc[0]['high'] - df.iloc[0]['low'])/df.iloc[0]['close'] 
    return target_percentEC   

def get_target_percentL(ticker):
    """변동성 돌파 전략에 전날 변동성 계산"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_percentL = (df.iloc[0]['high'] - df.iloc[0]['low'])/df.iloc[0]['close'] 
    return target_percentL                       

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

def get_ma15(ticker):
    """15일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15    

def get_ma5E(ticker):
    """5일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    ma5E = df['close'].rolling(5).mean().iloc[-1]
    return ma5E

def get_ma15E(ticker):
    """15일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15E = df['close'].rolling(15).mean().iloc[-1]
    return ma15E    

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

def get_ma15X(ticker):
    """15일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15X = df['close'].rolling(15).mean().iloc[-1]
    return ma15X         

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

def get_ma5EC(ticker):
    """5일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    ma5EC = df['close'].rolling(5).mean().iloc[-1]
    return ma5EC  

def get_ma10EC(ticker):
    """10일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=10)
    ma10EC = df['close'].rolling(10).mean().iloc[-1]
    return ma10EC

def get_ma20EC(ticker):
    """20일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=20)
    ma20EC = df['close'].rolling(20).mean().iloc[-1]
    return ma20EC    

def get_ma5L(ticker):
    """5일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    ma5L = df['close'].rolling(5).mean().iloc[-1]
    return ma5L  

def get_ma10L(ticker):
    """10일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=10)
    ma10L = df['close'].rolling(10).mean().iloc[-1]
    return ma10L  

def get_ma20L(ticker):
    """20일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=20)
    ma20L = df['close'].rolling(20).mean().iloc[-1]
    return ma20L                           

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

def get_current_priceEC(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"] 

def get_current_priceL(ticker):
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

        open_price = get_open_price("KRW-BTC")
        current_price = get_current_price("KRW-BTC")
        target_price = get_target_price("KRW-BTC", 0.5)
        ma5 = get_ma5("KRW-BTC")
        ma15 = get_ma15("KRW-BTC")
        target_percent = get_target_percent("KRW-BTC") 

        open_priceE = get_open_priceE("KRW-ETH")
        current_priceE = get_current_priceE("KRW-ETH") 
        target_priceE = get_target_priceE("KRW-ETH", 0.5) 
        ma5E = get_ma5E("KRW-ETH")
        ma15E = get_ma15E("KRW-ETH")        
        target_percentE = get_target_percentE("KRW-ETH")

        open_priceX = get_open_priceE("KRW-XRP")
        current_priceX = get_current_priceE("KRW-XRP") 
        target_priceX = get_target_priceX("KRW-XRP", 0.5)
        ma5X = get_ma5X("KRW-XRP")
        ma10X = get_ma10X("KRW-XRP")
        ma15X = get_ma15X("KRW-XRP")
        target_percentX = get_target_percentX("KRW-XRP")

        open_priceA = get_open_priceE("KRW-ADA")
        current_priceA = get_current_priceE("KRW-ADA")
        target_priceA = get_target_priceA("KRW-ADA", 0.5)
        ma5A = get_ma5A("KRW-ADA")
        ma10A = get_ma10A("KRW-ADA")
        target_percentA = get_target_percentA("KRW-ADA")


        open_priceEC = get_open_priceEC("KRW-ETC")
        current_priceEC = get_current_priceEC("KRW-ETC")
        target_priceEC = get_target_priceEC("KRW-ETC", 0.5)
        ma5EC = get_ma5EC("KRW-ETC")
        ma10EC = get_ma10EC("KRW-ETC")
        ma20EC = get_ma20EC("KRW-ETC")        
        target_percentEC = get_target_percentEC("KRW-ETC")

        open_priceL = get_open_priceL("KRW-SOL")
        current_priceL = get_current_priceL("KRW-SOL")
        target_priceL = get_target_priceL("KRW-SOL", 0.5)
        ma5L = get_ma5L("KRW-SOL")
        ma10L = get_ma10L("KRW-SOL")
        ma20L = get_ma20L("KRW-SOL")
        target_percentL = get_target_percentL("KRW-SOL")




        if start_time < now < end_time - datetime.timedelta(minutes=10) and current_price > target_price*0.95 :

            if target_price < current_price and ma15 < current_price:
                krw = get_balance("KRW")
                btc = get_balance("BTC")
                if target_percent  <= 0.015:
                    if btc < 0.0001:
                        buy_result = upbit.buy_market_order("KRW-BTC", krw*(0.5))
                        post_message(myToken,"#crypto", "BTC buy : " +str(buy_result))
                elif 0.015 < target_percent:
                    if btc < 0.0001:
                        buy_result = upbit.buy_market_order("KRW-BTC", krw*(1/target_percent/130))
                        post_message(myToken,"#crypto", "BTC buy : " +str(buy_result))

        else:
            btc = get_balance("BTC")
            if btc > 0.00004:
                sell_result = upbit.sell_market_order("KRW-BTC", btc)
                post_message(myToken,"#crypto", "BTC buy : " +str(sell_result))


        if start_time < now < end_time - datetime.timedelta(minutes=10) and current_priceE > target_priceE*0.95 :
            if target_priceE < current_priceE and ma15E < current_priceE:
                krw = get_balance("KRW")
                eth = get_balance("ETH")
                if target_percentE  <= 0.015:
                    if eth < 0.0005:
                        buy_result = upbit.buy_market_order("KRW-ETH", krw*(0.5))
                        post_message(myToken,"#crypto", "ETH buy : " +str(buy_result))
                elif 0.015 < target_percentE:
                    if eth < 0.0005:
                        buy_result = upbit.buy_market_order("KRW-ETH", krw*(1/target_percentE/130))
                        post_message(myToken,"#crypto", "ETH buy : " +str(buy_result))

        else:               
            eth = get_balance("ETH")
            if eth > 0.0001:
                sell_result = upbit.sell_market_order("KRW-ETH", eth)
                post_message(myToken,"#crypto", "ETH buy : " +str(sell_result))                             
                                 
        if start_time < now < end_time - datetime.timedelta(minutes=10) and current_priceX > target_priceX*0.95 :
            if target_priceX < current_priceX and ma15X < current_priceX:
                krw = get_balance("KRW")
                xrp = get_balance("XRP")
                if target_percentX  <= 0.015:
                    if xrp < 0.01:
                        buy_result = upbit.buy_market_order("KRW-XRP", krw*(0.5))
                        post_message(myToken,"#crypto", "XRP buy : " +str(buy_result))
                elif 0.015 < target_percentX:
                    if xrp < 0.01:
                        buy_result = upbit.buy_market_order("KRW-XRP", krw*(1/target_percentX/140))
                        post_message(myToken,"#crypto", "XRP buy : " +str(buy_result))

        else:               
            xrp = get_balance("XRP")
            if xrp > 0.001:
                sell_result = upbit.sell_market_order("KRW-XRP", xrp)
                post_message(myToken,"#crypto", "XRP buy : " +str(sell_result))  

        if start_time < now < end_time - datetime.timedelta(minutes=10) and current_priceA > target_priceA*0.95 : 
            if target_priceA < current_priceA and ma5A < current_priceA and ma10A < current_priceA:
                krw = get_balance("KRW")
                ada = get_balance("ADA")
                if target_percentA  <= 0.015:
                    if ada < 0.01:
                        buy_result = upbit.buy_market_order("KRW-ADA", krw*(0.5))
                        post_message(myToken,"#crypto", "ADA buy : " +str(buy_result))
                elif 0.015 < target_percentA:
                    if ada < 0.01:
                        buy_result = upbit.buy_market_order("KRW-ADA", krw*(1/target_percentA/140))
                        post_message(myToken,"#crypto", "ADA buy : " +str(buy_result))

        else:               
            ada = get_balance("ADA")
            if ada > 0.001:
                sell_result = upbit.sell_market_order("KRW-ADA", ada)
                post_message(myToken,"#crypto", "ADA buy : " +str(sell_result))                                    

        if start_time < now < end_time - datetime.timedelta(minutes=10) and current_priceEC > target_priceEC*0.95 : 
            if target_priceEC < current_priceEC and ma20EC < current_priceEC:
                krw = get_balance("KRW")
                etc = get_balance("ETC")
                if target_percentA  <= 0.015:
                    if etc < 0.01:
                        buy_result = upbit.buy_market_order("KRW-ETC", krw*(0.4))
                        post_message(myToken,"#crypto", "ETC buy : " +str(buy_result))
                elif 0.015 < target_percentA:
                    if etc < 0.01:
                        buy_result = upbit.buy_market_order("KRW-ETC", krw*(1/target_percentEC/170))
                        post_message(myToken,"#crypto", "ETC buy : " +str(buy_result))

        else:               
            etc = get_balance("ETC")
            if etc > 0.001:
                sell_result = upbit.sell_market_order("KRW-ETC", etc)
                post_message(myToken,"#crypto", "ETC buy : " +str(sell_result))    

        if start_time < now < end_time - datetime.timedelta(minutes=10) and current_priceL > target_priceL*0.95 :
            if target_priceL < current_priceL and ma20L < current_priceL:
                krw = get_balance("KRW")
                sol = get_balance("SOL")
                if target_percentL  <= 0.015:
                    if sol < 0.01:
                        buy_result = upbit.buy_market_order("KRW-SOL", krw*(0.4))
                        post_message(myToken,"#crypto", "SOL buy : " +str(buy_result))
                elif 0.015 < target_percentA:
                    if sol < 0.01:
                        buy_result = upbit.buy_market_order("KRW-SOL", krw*(1/target_percentL/170))
                        post_message(myToken,"#crypto", "SOL buy : " +str(buy_result))

        else:               
            sol = get_balance("SOL")
            if sol > 0.001:
                sell_result = upbit.sell_market_order("KRW-SOL", sol)
                post_message(myToken,"#crypto", "SOL buy : " +str(sell_result))   



                
        time.sleep(1)
    except Exception as e:
        print(e)
        post_message(myToken,"#crypto", e)
        time.sleep(1)