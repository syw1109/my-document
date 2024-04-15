import time
import pyupbit
import datetime


#231207 ma20 *0.997 이상이면 사지는 조건 추가
#240322 SOL추가 추가
access = "VjbtLbzbFoAVeILkHwCC4PFc5l8lcfQJghzBVBmD"
secret = "gL8xagr10FdayU7dWjtI5XZ1pwratIbe9xjy9Jc9"

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

def get_open_priceo(ticker):
    """09:00 시작가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    open_priceo = df.iloc[0]['close']
    return open_priceo 

   

#오늘의 최저가 low가 ma20,30보다 높은지 확인하기 위함  [1] 오늘 저가
def get_low_price(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    low_price = df.iloc[1]['low']
    return low_price  

def get_low_priceE(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    low_priceE = df.iloc[1]['low']
    return low_priceE     


def get_low_priceo(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    low_priceo = df.iloc[1]['low']
    return low_priceo 

   


def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_ma20(ticker):
    """20일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=21)
    df['hykin'] = (df['high'] + df['low']+df['open']+df['close'])/4
    ma20 = df['hykin'].rolling(20).mean().iloc[-2]
    return ma20 

def get_ma20E(ticker):
    """20일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=21)
    ma20E = df['close'].rolling(20).mean().iloc[-2]
    return ma20E    

# def get_ma30(ticker):
#     """30일 이동 평균선 조회"""
#     df = pyupbit.get_ohlcv(ticker, interval="day", count=31)
#     ma30 = df['close'].rolling(30).mean().iloc[-2]
#     return ma30

def get_ma30(ticker):
    """30일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=31)
    df['hykin'] = (df['high'] + df['low']+df['open']+df['close'])/4
    ma30 = df['hykin'].rolling(30).mean().iloc[-2]
    return ma30   

def get_ma30E(ticker):
    """30일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=31)
    ma30E = df['close'].rolling(30).mean().iloc[-2]
    return ma30E  


def get_ma16o(ticker):
    """16일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=17)
    ma16o = df['close'].rolling(16).mean().iloc[-2]
    return ma16o   



def get_ma44o(ticker):
    """44일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=45)
    ma44o = df['close'].rolling(44).mean().iloc[-2]
    return ma44o        
   

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

def get_current_priceo(ticker):
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
        end_time = start_time + datetime.timedelta(minutes=2)
        end_time1 = start_time + datetime.timedelta(minutes=1)

        open_price = get_open_price("KRW-BTC")
        low_price = get_low_price("KRW-BTC")
        current_price = get_current_price("KRW-BTC")
        ma20 = get_ma20("KRW-BTC")
        ma30 = get_ma30("KRW-BTC")        
        


        open_priceE = get_open_priceE("KRW-ETH")
        low_priceE = get_low_priceE("KRW-ETH")        
        current_priceE = get_current_priceE("KRW-ETH")
        ma20E = get_ma20E("KRW-ETH")
        ma30E = get_ma30E("KRW-ETH")        
        
        
      
        

        krw = get_balance("KRW")
        btc = get_balance("BTC")
        eth = get_balance("ETH")
        sol = get_balance("SOL")
        
        print(btc)
        print(eth)
        print(sol)
        
        open_priceS = get_open_priceS("KRW-SOL")      # --->   'NoneType' object is not subscriptable
        low_priceS = get_low_priceS("KRW-SOL")      # --->   'NoneType' object is not subscriptable
        current_priceo = get_current_priceo("KRW-SOL")
        # ma16o = get_ma16o("KRW-SOL")     # --->   'NoneType' object is not subscriptable
        ma44o = get_ma44o("KRW-SOL")  
        

        if open_price < ma20*1.02 or open_price < ma30*1.02:
            if low_price > ma20*0.98 and low_price > ma30*0.98 and open_price > ma20*0.997 and open_price > ma30:  
                if end_time1 < now :
                    if eth < 0.01:
                        if btc < 0.0005:

                            buy_result = upbit.buy_market_order("KRW-BTC", krw*(0.44))
                         
                    if eth > 0.01:
                        if btc < 0.0005:
 
                            buy_result = upbit.buy_market_order("KRW-BTC", krw*(0.999))

            else:
                if btc > 0.0005:
                    sell_result = upbit.sell_market_order("KRW-BTC", btc)                            

        if open_price > ma20*1.02 and open_price > ma30*1.02:
            if low_price > ma20 and low_price > ma30 and open_price > ma20 and open_price > ma30:  
                if end_time < now :
                    if eth < 0.01:
                        if btc < 0.0005:

                            buy_result = upbit.buy_market_order("KRW-BTC", krw*(0.44))
                         
                    if eth > 0.01:
                        if btc < 0.0005:
 
                            buy_result = upbit.buy_market_order("KRW-BTC", krw*(0.999))                            

            else:
                if btc > 0.0005:
                    sell_result = upbit.sell_market_order("KRW-BTC", btc)


        if open_priceE < ma20E*1.025 or open_priceE < ma30E*1.025:

            if low_priceE > ma20E*0.975 and low_priceE > ma30E*0.975 and open_priceE > ma20E*0.997 and open_priceE > ma30E:
                if end_time < now :

                    if btc < 0.0005:
                        if eth < 0.01:
                    
                            buy_result = upbit.buy_market_order("KRW-ETH", krw*(0.559))
                         
                    if btc > 0.0005:
                        if eth < 0.01:
                   
                            buy_result = upbit.buy_market_order("KRW-ETH", krw*(0.999))
            else:
                if eth > 0.01:
                    sell_result = upbit.sell_market_order("KRW-ETH", eth)                             

        if open_priceE > ma20E*1.025 and open_priceE > ma30E*1.025:

            if low_priceE > ma20E and low_priceE > ma30E and open_priceE > ma20E and open_priceE > ma30E:
                if end_time < now :

                    if btc < 0.0005:
                        if eth < 0.01:
                    
                            buy_result = upbit.buy_market_order("KRW-ETH", krw*(0.559))
                         
                    if btc > 0.0005:
                        if eth < 0.01:                    
                            buy_result = upbit.buy_market_order("KRW-ETH", krw*(0.999))

            else:
                if eth > 0.01:
                    sell_result = upbit.sell_market_order("KRW-ETH", eth)        
                    
                    
        # if open_priceS < ma16S*1.07 or open_priceS < ma44S*1.07:
        #     if low_priceS > ma16S*0.98 and low_priceS > ma44S*0.98 and open_priceS > ma16S and open_priceS > ma44S:
        #         if end_time < now :

        #             if eth < 0.1 and btc <0.001:
        #                 if sol < 0.1:

        #                     buy_result = upbit.buy_market_order("KRW-SOL", krw*(0.3))
                         
        #             if eth > 0.1 and btc < 0.001:
        #                 if sol < 0.1:
 
        #                     buy_result = upbit.buy_market_order("KRW-SOL", krw*(0.43))
                            
        #             if eth < 0.1 and btc > 0.001:
        #                 if sol < 0.1:
 
        #                     buy_result = upbit.buy_market_order("KRW-SOL", krw*(0.43))                            
                            
        #             if eth > 0.1 and btc > 0.001:
        #                 if sol < 0.1:

        #                     buy_result = upbit.buy_market_order("KRW-SOL", krw*(0.999)) 

        #     else:
        #         if sol > 0.1:
        #             sell_result = upbit.sell_market_order("KRW-SOL", sol)                    
                    


        # if open_priceS > ma16S*1.07 and open_priceS > ma44S*1.07:

        #     if low_priceS > ma16S and low_priceS > ma44S and open_priceS > ma16S and open_priceS > ma44S:
        #         if end_time < now :

        #             if eth < 0.1 and btc <0.001:
        #                 if sol < 0.1:

        #                     buy_result = upbit.buy_market_order("KRW-SOL", krw*(0.3))
                         
        #             if eth > 0.1 and btc < 0.001:
        #                 if sol < 0.1:
 
        #                     buy_result = upbit.buy_market_order("KRW-SOL", krw*(0.43))
                            
        #             if eth < 0.1 and btc > 0.001:
        #                 if sol < 0.1:
 
        #                     buy_result = upbit.buy_market_order("KRW-SOL", krw*(0.43))                            
                            
        #             if eth > 0.1 and btc > 0.001:
        #                 if sol < 0.1:

        #                     buy_result = upbit.buy_market_order("KRW-SOL", krw*(0.999)) 

        #     else:
        #         if sol > 0.1:
        #             sell_result = upbit.sell_market_order("KRW-SOL", sol)     




        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)



