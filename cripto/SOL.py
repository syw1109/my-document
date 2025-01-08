import time
import pyupbit
import datetime


#231207 ma20 *0.997 이상이면 사지는 조건 추가
#240322 SOL추가 추가
access = "VjbtLbzbFoAVeILkHwCC4PFc5l8lcfQJghzBVBmD"
secret = "gL8xagr10FdayU7dWjtI5XZ1pwratIbe9xjy9Jc9"

#시작가가(어제의 종가) ma20, ma30 보다 높은지 확인하기 위함 [0]은 어제종가=오늘 시가 
 

def get_open_priceS(ticker):
    """09:00 시작가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    open_priceS = df.iloc[0]['close']
    return open_priceS   

#오늘의 최저가 low가 ma20,30보다 높은지 확인하기 위함  [1] 오늘 저가
  

def get_low_priceS(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    low_priceS = df.iloc[1]['low']
    return low_priceS  

   

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

  

def get_ma16S(ticker):
    """16일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=17)
    ma16S = df['close'].rolling(16).mean().iloc[-2]
    return ma16S   



def get_ma44S(ticker):
    """44일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=45)
    ma44S = df['close'].rolling(44).mean().iloc[-2]
    return ma44S         

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

def get_current_priceS(ticker):
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
        end_time = start_time + datetime.timedelta(minutes=1)
        end_time1 = start_time + datetime.timedelta(minutes=1)
       
        
        open_priceS = get_open_priceS("KRW-SOL")
        low_priceS = get_low_priceS("KRW-SOL")        
        current_priceS = get_current_priceS("KRW-SOL")
        ma16S = get_ma16S("KRW-SOL")
        ma44S = get_ma44S("KRW-SOL")             
        
      

        krw = get_balance("KRW")
        btc = get_balance("BTC")
        eth = get_balance("ETH")
        sol = get_balance("SOL")
        
        print(btc)
        print(sol)
        print(eth)

        




#sol1
        if open_priceS < ma16S*1.07 or open_priceS < ma44S*1.07:
            if low_priceS > ma16S*0.98 and low_priceS > ma44S*0.98 and open_priceS > ma16S and open_priceS > ma44S:
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
                if sol > 0.1:
                    sell_result = upbit.sell_market_order("KRW-SOL", sol)   
                    

#sol2
        if open_priceS > ma16S*1.07 and open_priceS > ma44S*1.07:

            if low_priceS > ma16S and low_priceS > ma44S and open_priceS > ma16S and open_priceS > ma44S:
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
                if sol > 0.1:
                    sell_result = upbit.sell_market_order("KRW-SOL", sol)                                           


        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)



