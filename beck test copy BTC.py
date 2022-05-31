
import pyupbit
import numpy as np

df = pyupbit.get_ohlcv("KRW-ETH", interval="day", count=4)
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)


df['0'] = df.iloc[0]['close']
df['1'] = df.iloc[1]['close']
df['-1'] = df.iloc[-1]['close']
df['3'] = df['close'].rolling(4).mean().iloc[-1]

df['eh'] = pyupbit.get_orderbook("KRW-ETH")["orderbook_units"][0]["ask_price"]


df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("eth.xlsx")