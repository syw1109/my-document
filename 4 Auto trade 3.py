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
    

def get_target_pricebch(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_pricebch = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_pricebch   

def get_target_priceltc(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_priceltc = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_priceltc

def get_target_pricexlm(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_pricexlm = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_pricexlm         

def get_target_priceeos(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    """ohlcv : 주식의 종가,시가, 최고,최저 정보 불러오는 함수"""
    """iloc : 인덱스 함수 [1]이 오늘, [0]은 어제"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_priceeos = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_priceeos                    
  


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
 

def get_open_pricebch(ticker):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    open_pricebch = df.iloc[0]['close']
    return open_pricebch  

def get_open_priceltc(ticker):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    open_priceltc = df.iloc[0]['close']
    return open_priceltc  

def get_open_pricexlm(ticker):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    open_pricexlm = df.iloc[0]['close']
    return open_pricexlm  

def get_open_priceeos(ticker):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    open_priceeos = df.iloc[0]['close']
    return open_priceeos              




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
 

def get_target_percentbch(ticker):
    """변동성 돌파 전략에 전날 변동성 계산"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_percentbch = (df.iloc[0]['high'] - df.iloc[0]['low'])/df.iloc[0]['close'] 
    return target_percentbch

def get_target_percentltc(ticker):
    """변동성 돌파 전략에 전날 변동성 계산"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_percentltc = (df.iloc[0]['high'] - df.iloc[0]['low'])/df.iloc[0]['close'] 
    return target_percentltc

def get_target_percentxlm(ticker):
    """변동성 돌파 전략에 전날 변동성 계산"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_percentxlm = (df.iloc[0]['high'] - df.iloc[0]['low'])/df.iloc[0]['close'] 
    return target_percentxlm

def get_target_percenteos(ticker):
    """변동성 돌파 전략에 전날 변동성 계산"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_percenteos = (df.iloc[0]['high'] - df.iloc[0]['low'])/df.iloc[0]['close'] 
    return target_percenteos



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

def get_ma5E(ticker):
    """5일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    ma5E = df['close'].rolling(5).mean().iloc[-1]
    return ma5E

def get_ma10E(ticker):
    """10일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=10)
    ma10E = df['close'].rolling(10).mean().iloc[-1]
    return ma10E        

def get_ma20E(ticker):
    """20일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=20)
    ma20E = df['close'].rolling(20).mean().iloc[-1]
    return ma20E    

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
   

def get_ma5bch(ticker):
    """5일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    ma5bch = df['close'].rolling(5).mean().iloc[-1]
    return ma5bch

def get_ma20bch(ticker):
    """20일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=20)
    ma20bch = df['close'].rolling(20).mean().iloc[-1]
    return ma20bch   

def get_ma5ltc(ticker):
    """5일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    ma5ltc = df['close'].rolling(5).mean().iloc[-1]
    return ma5ltc

def get_ma10ltc(ticker):
    """10일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=10)
    ma10ltc = df['close'].rolling(10).mean().iloc[-1]
    return ma10ltc    

def get_ma20ltc(ticker):
    """20일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=20)
    ma20ltc = df['close'].rolling(20).mean().iloc[-1]
    return ma20ltc   

def get_ma5xlm(ticker):
    """5일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    ma5xlm = df['close'].rolling(5).mean().iloc[-1]
    return ma5xlm

def get_ma20xlm(ticker):
    """20일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=20)
    ma20xlm = df['close'].rolling(20).mean().iloc[-1]
    return ma20xlm     

def get_ma5eos(ticker):
    """5일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    ma5eos = df['close'].rolling(5).mean().iloc[-1]
    return ma5eos   

def get_ma20eos(ticker):
    """20일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=20)
    ma20eos = df['close'].rolling(20).mean().iloc[-1]
    return ma20eos   


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
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(hours=24)

        open_price = get_open_price("KRW-BTC")
        current_price = get_current_price("KRW-BTC")
        target_price = get_target_price("KRW-BTC", 0.4)
        ma5 = get_ma5("KRW-BTC")
        ma20 = get_ma20("KRW-BTC")
        target_percent = get_target_percent("KRW-BTC") 

        open_priceE = get_open_priceE("KRW-ETH")
        current_priceE = get_current_priceE("KRW-ETH") 
        target_priceE = get_target_priceE("KRW-ETH", 0.25) 
        ma5E = get_ma5E("KRW-ETH")
        ma10E = get_ma10E("KRW-ETH")
        ma20E = get_ma20E("KRW-ETH")        
        target_percentE = get_target_percentE("KRW-ETH")

        open_priceX = get_open_priceX("KRW-XRP")
        current_priceX = get_current_priceX("KRW-XRP") 
        target_priceX = get_target_priceX("KRW-XRP", 0.5)
        ma5X = get_ma5X("KRW-XRP")
        ma10X = get_ma10X("KRW-XRP")
        ma20X = get_ma20X("KRW-XRP")
        target_percentX = get_target_percentX("KRW-XRP")

        open_priceA = get_open_priceA("KRW-ADA")
        current_priceA = get_current_priceA("KRW-ADA")
        target_priceA = get_target_priceA("KRW-ADA", 0.5)
        ma5A = get_ma5A("KRW-ADA")
        ma10A = get_ma10A("KRW-ADA")
        target_percentA = get_target_percentA("KRW-ADA")

        open_pricebch = get_open_pricebch("KRW-BCH")
        current_pricebch = get_current_pricebch("KRW-BCH")
        target_pricebch = get_target_pricebch("KRW-BCH", 0.3)
        ma5bch = get_ma5bch("KRW-BCH")
        ma20bch = get_ma20bch("KRW-BCH")
        target_percentbch = get_target_percentbch("KRW-BCH") 

        open_priceltc = get_open_priceltc("KRW-LTC")
        current_priceltc = get_current_priceltc("KRW-LTC")
        target_priceltc = get_target_priceltc("KRW-LTC", 0.1)
        ma5ltc = get_ma5ltc("KRW-LTC")
        ma10ltc = get_ma10ltc("KRW-LTC")        
        ma20ltc = get_ma20ltc("KRW-LTC")
        target_percentltc = get_target_percentltc("KRW-LTC")         

        open_pricexlm = get_open_pricexlm("KRW-XLM")
        current_pricexlm = get_current_pricexlm("KRW-XLM")
        target_pricexlm = get_target_pricexlm("KRW-XLM", 0.1)
        ma5xlm = get_ma5xlm("KRW-XLM")
        ma20xlm = get_ma20xlm("KRW-XLM")
        target_percentxlm = get_target_percentxlm("KRW-XLM") 

        open_priceeos = get_open_priceeos("KRW-EOS")
        current_priceeos = get_current_priceeos("KRW-EOS")
        target_priceeos = get_target_priceeos("KRW-EOS", 0.1)
        ma5eos = get_ma5eos("KRW-EOS")
        ma20eos = get_ma20eos("KRW-EOS")
        target_percenteos = get_target_percenteos("KRW-EOS")         


        if start_time < now < end_time - datetime.timedelta(minutes=10)  :

            if target_price < current_price and ma5 < current_price and ma20 < current_price:
                krw = get_balance("KRW")
                btc = get_balance("BTC")
                if target_percent  <= 0.015:
                    if btc < 0.0001:
                        buy_result = upbit.buy_market_order("KRW-BTC", krw*(0.17))
                elif 0.015 < target_percent:
                    if btc < 0.0001:
                        buy_result = upbit.buy_market_order("KRW-BTC", krw*(1/target_percent/420))

        else:
            btc = get_balance("BTC")
            if btc > 0.00004:
                sell_result = upbit.sell_market_order("KRW-BTC", btc)



        if start_time < now < end_time - datetime.timedelta(minutes=10)  :
            if target_priceE < current_priceE and ma5E < current_priceE and ma20E < current_priceE and ma10E < current_priceE:
                krw = get_balance("KRW")
                eth = get_balance("ETH")
                if target_percentE  <= 0.015:
                    if eth < 0.0005:
                        buy_result = upbit.buy_market_order("KRW-ETH", krw*(0.13))

                elif 0.015 < target_percentE:
                    if eth < 0.0005:
                        buy_result = upbit.buy_market_order("KRW-ETH", krw*(1/target_percentE/550))


        else:               
            eth = get_balance("ETH")
            if eth > 0.0001:
                sell_result = upbit.sell_market_order("KRW-ETH", eth)
                         
                                 
        if start_time < now < end_time - datetime.timedelta(minutes=10) :
            if target_priceX < current_priceX and ma5X < current_priceX and ma10X < current_priceX:
                krw = get_balance("KRW")
                xrp = get_balance("XRP")
                if target_percentX  <= 0.015:
                    if xrp < 0.01:
                        buy_result = upbit.buy_market_order("KRW-XRP", krw*(0.2))

                elif 0.015 < target_percentX:
                    if xrp < 0.01:
                        buy_result = upbit.buy_market_order("KRW-XRP", krw*(1/target_percentX/400))


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
                        buy_result = upbit.buy_market_order("KRW-ADA", krw*(0.2))

                elif 0.015 < target_percentA:
                    if ada < 0.01:
                        buy_result = upbit.buy_market_order("KRW-ADA", krw*(1/target_percentA/400))

        else:               
            ada = get_balance("ADA")
            if ada > 0.001:
                sell_result = upbit.sell_market_order("KRW-ADA", ada)
                                  


        if start_time < now < end_time - datetime.timedelta(minutes=10) :

            if target_pricebch < current_pricebch and ma5bch < current_pricebch and ma20bch < current_pricebch:
                krw = get_balance("KRW")
                bch = get_balance("BCH")
                if target_percentbch  <= 0.015:
                    if bch < 0.01:
                        buy_result = upbit.buy_market_order("KRW-BCH", krw*(0.1))

                elif 0.015 < target_percentbch:
                    if bch < 0.01:
                        buy_result = upbit.buy_market_order("KRW-BCH", krw*(1/target_percentbch/650))

        else:
            bch = get_balance("BCH")
            if bch > 0.004:
                sell_result = upbit.sell_market_order("KRW-BCH", bch)

        if start_time < now < end_time - datetime.timedelta(minutes=10) :

            if target_priceltc < current_priceltc and ma5ltc < current_priceltc and ma10ltc < current_priceltc and ma20ltc < current_priceltc:
                krw = get_balance("KRW")
                ltc = get_balance("LTC")
                if target_percentltc  <= 0.015:
                    if ltc < 0.01:
                        buy_result = upbit.buy_market_order("KRW-LTC", krw*(0.1))

                elif 0.015 < target_percentltc:
                    if ltc < 0.01:
                        buy_result = upbit.buy_market_order("KRW-LTC", krw*(1/target_percentltc/600))

        else:
            ltc = get_balance("LTC")
            if ltc > 0.004:
                sell_result = upbit.sell_market_order("KRW-LTC", ltc)

        if start_time < now < end_time - datetime.timedelta(minutes=10) :

            if target_pricexlm < current_pricexlm and ma5xlm < current_pricexlm and ma20xlm < current_pricexlm:
                krw = get_balance("KRW")
                xlm = get_balance("XLM")
                if target_percentxlm  <= 0.015:
                    if xlm < 1:
                        buy_result = upbit.buy_market_order("KRW-XLM", krw*(0.1))

                elif 0.015 < target_percentxlm:
                    if xlm < 1:
                        buy_result = upbit.buy_market_order("KRW-XLM", krw*(1/target_percentxlm/650))

        else:
            xlm = get_balance("XLM")
            if xlm > 0.4:
                sell_result = upbit.sell_market_order("KRW-XLM", xlm)


        if start_time < now < end_time - datetime.timedelta(minutes=10) :

            if target_priceeos < current_priceeos and ma5eos < current_priceeos and ma20eos < current_priceeos:
                krw = get_balance("KRW")
                eos = get_balance("EOS")
                if target_percenteos  <= 0.015:
                    if eos < 0.1:
                        buy_result = upbit.buy_market_order("KRW-EOS", krw*(0.1))

                elif 0.015 < target_percenteos:
                    if eos < 0.1:
                        buy_result = upbit.buy_market_order("KRW-EOS", krw*(1/target_percenteos/700))

        else:
            eos = get_balance("EOS")
            if eos > 0.04:
                sell_result = upbit.sell_market_order("KRW-EOS", eos)                


                
        time.sleep(1)
    except Exception as e:
        print(e)
        post_message(myToken,"#crypto", e)
        time.sleep(1)