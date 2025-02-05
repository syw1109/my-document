import time
import pyupbit
import datetime


#231207 ma20 *0.997 이상이면 사지는 조건 추가
#240322 SOL추가 추가
#240426 비트코인 하이킨+31,45  솔라나 High 기준  ma16 high가 좋고, maa44 close 가 좋더라
# 250204 상승장에선 오픈 기준이 맞더라. 중간에 매도 nono, 마켓메이커가 개미털기 많이함.
# 250204 시가 기준에서는 비트코인 하이킨 안해도 되더라
# 250204 ma31 *0.997 조건 제거

access = "BGwwKGFoVeaPOoh6qnWgnQllH8DFSCyzXR2IXVH4"
secret = "TCDxpnKdCXxTuZaMrUgK5zDICxHessZtjqTvZCRf"

#시작가가(어제의 종가) ma20, ma30 보다 높은지 확인하기 위함 [0]은 어제종가=오늘 시가 
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

def get_open_priceS(ticker):
    """09:00 시작가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    open_priceS = df.iloc[0]['close']
    return open_priceS   

#오늘의 최저가 low가 ma20,30보다 높은지 확인하기 위함  [1] 오늘 저가
# def get_low_price(ticker):
#     df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
#     low_price = df.iloc[1]['low']
#     return low_price  

# def get_low_priceE(ticker):
#     df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
#     low_priceE = df.iloc[1]['low']
#     return low_priceE   

# def get_low_priceS(ticker):
#     df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
#     low_priceS = df.iloc[1]['low']
#     return low_priceS  

   

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

# def get_ma20(ticker):
#     """20일 이동 평균선 조회"""
#     df = pyupbit.get_ohlcv(ticker, interval="day", count=22)
#     ma20 = df['close'].rolling(20).mean().iloc[-2]
#     return ma20 

def get_ma31(ticker):
    """31일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=32)
    ma31 = df['close'].rolling(31).mean().iloc[-2]
    return ma31


def get_ma20E(ticker):
    """20일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=21)
    ma20E = df['close'].rolling(20).mean().iloc[-2]
    return ma20E  

def get_ma16S(ticker):
    """16일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=17)
    ma16S = df['high'].rolling(16).mean().iloc[-2]
    return ma16S   


def get_ma45(ticker):
    """45일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=46)
    ma45 = df['close'].rolling(45).mean().iloc[-2]
    return ma45   

def get_ma30E(ticker):
    """30일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=31)
    ma30E = df['close'].rolling(30).mean().iloc[-2]
    return ma30E

def get_ma43S(ticker):
    """44일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=44)
    ma43S = df['close'].rolling(43).mean().iloc[-2]
    return ma43S         

#---------------------------------------------------     

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

# def get_current_price(ticker):
#     """현재가 조회"""
#     return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# def get_current_priceE(ticker):
#     """현재가 조회"""
#     return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]  

# def get_current_priceS(ticker):
#     """현재가 조회"""
#     return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]    

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(minutes=0.1)
        end_time1 = start_time + datetime.timedelta(minutes=0.5)
        end_time2 = start_time + datetime.timedelta(minutes=0.7)

        open_price = get_open_price("KRW-BTC")
        # low_price = get_low_price("KRW-BTC")
        # current_price = get_current_price("KRW-BTC")
        ma31 = get_ma31("KRW-BTC")
        ma45 = get_ma45("KRW-BTC")        


        open_priceE = get_open_priceE("KRW-ETH")
        # low_priceE = get_low_priceE("KRW-ETH")        
        # current_priceE = get_current_priceE("KRW-ETH")
        ma20E = get_ma20E("KRW-ETH")
        ma30E = get_ma30E("KRW-ETH")        
        
        
        open_priceS = get_open_priceS("KRW-SOL")
        # low_priceS = get_low_priceS("KRW-SOL")        
        # current_priceS = get_current_priceS("KRW-SOL")
        ma16S = get_ma16S("KRW-SOL")
        ma43S = get_ma43S("KRW-SOL")             
        
      
        krw = get_balance("KRW")
        btc = get_balance("BTC")
        eth = get_balance("ETH")
        sol = get_balance("SOL")
      
 
        
#btc1

        if open_price > ma31 and open_price > ma45:  
            if end_time2 < now :
                if eth < 0.01 and sol<0.05:
                    if btc < 0.0005:

                        buy_result = upbit.buy_market_order("KRW-BTC", krw*(0.4))
                         
                if eth > 0.01 and sol < 0.05:
                    if btc < 0.0005:
 
                        buy_result = upbit.buy_market_order("KRW-BTC", krw*(0.57))
                            
                if eth < 0.01 and sol > 0.05:
                    if btc < 0.0005:
 
                        buy_result = upbit.buy_market_order("KRW-BTC", krw*(0.57))                            
                            
                if eth > 0.01 and sol > 0.05:
                    if btc < 0.0005:

                        buy_result = upbit.buy_market_order("KRW-BTC", krw*(0.999))                            
                            
        else:
            if end_time2 < now :
                if btc > 0.0005:
                    sell_result = upbit.sell_market_order("KRW-BTC", btc) 
                    
                                              

# eth1

        if open_priceE > ma20E and open_priceE > ma30E:
            if end_time1 < now :

                if btc < 0.001 and sol<0.05:
                    if eth < 0.001:

                        buy_result = upbit.buy_market_order("KRW-ETH", krw*(0.3))
                         
                if btc > 0.001 and sol < 0.05:
                    if eth < 0.001:
 
                        buy_result = upbit.buy_market_order("KRW-ETH", krw*(0.43))
                            
                if btc < 0.001 and sol > 0.05:
                    if eth < 0.001:
 
                        buy_result = upbit.buy_market_order("KRW-ETH", krw*(0.43))                            
                            
                if btc > 0.001 and sol > 0.05:
                    if eth < 0.001:

                        buy_result = upbit.buy_market_order("KRW-ETH", krw*(0.999)) 
        else:
            if end_time1 < now :
                if eth > 0.01:
                    sell_result = upbit.sell_market_order("KRW-ETH", eth)                             




#sol1
        if open_priceS > ma16S and open_priceS > ma43S:

            if end_time < now :

                if eth < 0.1 and btc <0.001:
                    if sol < 0.1:

                        buy_result = upbit.buy_market_order("KRW-SOL", krw*(0.3))
                         
                if eth > 0.1 and btc < 0.001:
                    if sol < 0.1:
 
                        buy_result = upbit.buy_market_order("KRW-SOL", krw*(0.43))
                            
                if eth < 0.1 and btc > 0.001:
                    if sol < 0.1:
 
                        buy_result = upbit.buy_market_order("KRW-SOL", krw*(0.43))                            
                            
                if eth > 0.1 and btc > 0.001:
                    if sol < 0.1:

                        buy_result = upbit.buy_market_order("KRW-SOL", krw*(0.999)) 

        else:
            if end_time < now :
                if sol > 0.05:
                    sell_result = upbit.sell_market_order("KRW-SOL", sol)   
                    
                                     


        time.sleep(20)
    except Exception as e:
        print(e)
        time.sleep(10)



