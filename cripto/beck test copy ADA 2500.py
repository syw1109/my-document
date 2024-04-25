import pyupbit
import numpy as np
import pandas as pd

# OHLCV(open, high, low, close, volume)로 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터
df = pyupbit.get_ohlcv("KRW-ADA", count=5000)

pd.set_option('display.float_format', lambda x: '%.1f' % x)

df['ema5'] = df['close'].ewm(span=5, adjust=False).mean()
df['ema10'] = df['close'].ewm(span=10, adjust=False).mean()

df['ema20'] = df['close'].ewm(span=20, adjust=False).mean()
df['ema30'] = df['close'].ewm(span=30, adjust=False).mean()
df['ema50'] = df['close'].ewm(span=50, adjust=False).mean()

# 변동폭 * k 계산, (고가 - 저가) * k값
df['range'] = (df['high'] - df['low']) * 0.5

# target(매수가), range 컬럼을 한칸씩 밑으로 내림(.shift(1))
df['target'] = df['open'] + df['range'].shift(1)

# ror(수익률), np.where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)


# 누적 곱 계산(cumprod) => 누적 수익률
df['hpr'] = df['ror'].cumprod()

# Draw Down 계산 (누적 최대 값과 현재 hpr 차이 / 누적 최대값 * 100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

#MDD 계산
print("MDD(%): ", df['dd'].max())

#엑셀로 출력
df.to_excel("ada.xlsx")