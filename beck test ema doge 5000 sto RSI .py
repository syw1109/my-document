import pyupbit
import numpy as np
import pandas as pd

# OHLCV(open, high, low, close, volume) 데이터 가져오기
df = pyupbit.get_ohlcv("KRW-DOGE", count=5000)

def calculate_stoch_rsi(data, period=14, smoothK=3, smoothD=3):
    # 일반 RSI 계산
    delta = data['close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    # 스토캐스틱 RSI 계산
    stoch_rsi = (rsi - rsi.rolling(window=period).min()) / (rsi.rolling(window=period).max() - rsi.rolling(window=period).min())
    
    # %K와 %D 계산
    K = stoch_rsi.rolling(window=smoothK).mean() * 100
    D = K.rolling(window=smoothD).mean()
    
    return pd.DataFrame({'RSI': rsi, 'StochRSI_K': K, 'StochRSI_D': D})

# 스토캐스틱 RSI 계산
stoch_rsi_data = calculate_stoch_rsi(df, period=14, smoothK=3, smoothD=3)

# 결과를 원본 데이터와 결합
result = pd.concat([df, stoch_rsi_data], axis=1)

# 결과를 엑셀 파일로 저장
result.to_excel("DOGE_with_stoch_rsi.xlsx")