import ccxt
import numpy as np
import pandas as pd


# 바이낸스 객체 생성 (공개 API만 사용하는 경우 키/시크릿 없어도 됨)
exchange = ccxt.binance()
symbol = 'ETH/USDT'
timeframe = '1h'  # 1일봉


# OHLCV 데이터 가져오기 (ccxt의 fetch_ohlcv)
ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=500000)   # 최근 5000개 봉


# pandas DataFrame으로 변환
df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df.set_index('timestamp', inplace=True)
df.sort_index(inplace=True)  # 시간 순 정렬


def calculate_ema(data, period):
    return data.ewm(span=period, adjust=False).mean()


def calculate_stoch_rsi(data, period=14, smoothK=3, smoothD=3):
    # RSI 계산 (EMA 사용)
    delta = data['close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    
    avg_gain = calculate_ema(gain, period)
    avg_loss = calculate_ema(loss, period)
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    # 스토캐스틱 RSI
    stoch_rsi = (rsi - rsi.rolling(window=period).min()) / \
                (rsi.rolling(window=period).max() - rsi.rolling(window=period).min())
    
    # %K와 %D
    K = stoch_rsi.rolling(window=smoothK).mean() * 100
    D = K.rolling(window=smoothD).mean()
    
    return pd.DataFrame({'RSI': rsi, 'StochRSI_K': K, 'StochRSI_D': D})


# 스토캐스틱 RSI 계산
stoch_rsi_data = calculate_stoch_rsi(df, period=14, smoothK=3, smoothD=3)


# 원본 OHLCV와 결합
result = pd.concat([df, stoch_rsi_data], axis=1)


# 엑셀로 저장
result.to_excel("ETHUSDT_500000h.xlsx")


print("Data shape:", result.shape)
print("Date range:", result.index.min(), " ~ ", result.index.max())