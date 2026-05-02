import ccxt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time


exchange = ccxt.binance()
symbol = 'SOL/USDT'
timeframe = '1d'  # 1시간봉 → 1일봉으로 변경


# 5년 전 타임스탬프(ms)
five_years_ago = datetime.now() - timedelta(days=365 * 10)
since = int(five_years_ago.timestamp() * 1000)

# 반복 호출로 1일봉 가져오기
all_ohlcv = []
limit_per_call = 1000  # 바이낸스 최대 1000

while True:
    ohlcv = exchange.fetch_ohlcv(
        symbol,
        timeframe,
        since=since,
        limit=limit_per_call
    )
    if len(ohlcv) == 0:
        break

    all_ohlcv.extend(ohlcv)
    since = ohlcv[-1][0] + 1  # 마지막 봉 시점 다음부터
    time.sleep(1)  # Rate limit 대비


# DataFrame으로 변환
df = pd.DataFrame(all_ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df.set_index('timestamp', inplace=True)
df.sort_index(inplace=True)


# 날짜 옆에 요일 한글 컬럼 추가
ko_weekdays = ['월', '화', '수', '목', '금', '토', '일']
df['weekday'] = df.index.dayofweek.map(lambda x: ko_weekdays[x])


# EMA 계산
def calculate_ema(data, period):
    return data.ewm(span=period, adjust=False).mean()


# 스토캐스틱 RSI 계산
def calculate_stoch_rsi(data, period=14, smoothK=3, smoothD=3):
    delta = data['close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = calculate_ema(gain, period)
    avg_loss = calculate_ema(loss, period)

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    stoch_rsi = (rsi - rsi.rolling(window=period).min()) / \
                (rsi.rolling(window=period).max() - rsi.rolling(window=period).min())

    K = stoch_rsi.rolling(window=smoothK).mean() * 100
    D = K.rolling(window=smoothD).mean()

    return pd.DataFrame({'RSI': rsi, 'StochRSI_K': K, 'StochRSI_D': D})


# 스토캐스틱 RSI 계산
stoch_rsi_data = calculate_stoch_rsi(df, period=14, smoothK=3, smoothD=3)


# 원본 OHLCV + 요일 + RSI/스토캐스틱 RSI 결합
result = pd.concat([df, stoch_rsi_data], axis=1)


# 엑셀로 저장
result.to_excel("SOLUSDT_5years_1D_with_weekday.xlsx")


print("Data shape:", result.shape)
print("Date range:", result.index.min(), " ~ ", result.index.max())