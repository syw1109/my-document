import datetime
import numpy as np
import ccxt
import pandas as pd
# import sys
# sys.path.append("C:\python38-32\Lib\site-packages")


# python -m pip install ccxt 관리자모드로 실행해야 cctx가 깔린다
# pip install ccxt 
# 가상 환경 비활성화  deactivate, 다시 활성화 activate
# OHLCV(open, high, low, close, volume)로 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터

binance = ccxt.binance()
btc_ohlcv = binance.fetch_ohlcv("BTC/USDT", '1d')

df = pd.DataFrame(btc_ohlcv, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
df.set_index('datetime', inplace=True)
print(df)



#엑셀로 출력
df.to_excel("btcusdt.xlsx")