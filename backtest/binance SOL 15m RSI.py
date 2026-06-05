import ccxt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time

exchange = ccxt.binance()
symbol = 'SOL/USDT'
timeframe = '15m'

# ===================== 데이터 수집 =====================

five_years_ago = datetime.now() - timedelta(days=365 * 5)
since = int(five_years_ago.timestamp() * 1000)

all_ohlcv = []
limit_per_call = 1000

print("데이터 수집 시작...")
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
    since = ohlcv[-1][0] + 1
    print(f"  수집 중: {len(all_ohlcv)}개 ({pd.to_datetime(ohlcv[-1][0], unit='ms')})")
    time.sleep(1)

df = pd.DataFrame(all_ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df.set_index('timestamp', inplace=True)
df.sort_index(inplace=True)
df = df[~df.index.duplicated(keep='last')]  # 중복 제거

print(f"수집 완료: {len(df)}개 봉")


# ===================== Wilder(RMA) 방식 RSI 계산 =====================
# 일반 EMA 방식과의 차이:
#   - EMA 방식: 매 봉마다 지수 가중 (과거 봉 영향이 빠르게 감소)
#   - Wilder 방식: 첫 값은 단순 평균, 이후 (이전값 * (n-1) + 현재값) / n
#                  TradingView 기본 RSI와 동일한 방식
#                  과거 봉의 영향이 더 오래 지속되어 RSI가 더 완만하게 움직임

def calculate_wilder_rsi(close: pd.Series, rsi_length: int = 14) -> pd.Series:
    """
    Wilder(RMA) 방식 RSI 계산
    - 첫 avg_gain/avg_loss: rsi_length개 구간의 단순 평균
    - 이후: (이전값 * (rsi_length-1) + 현재값) / rsi_length
    - TradingView RSI와 동일한 결과
    """
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = (-delta).clip(lower=0)

    avg_gain = pd.Series(index=close.index, dtype='float64')
    avg_loss = pd.Series(index=close.index, dtype='float64')

    # 첫 번째 평균값: 1번~rsi_length번 봉의 단순 평균
    avg_gain.iloc[rsi_length] = gain.iloc[1:rsi_length + 1].mean()
    avg_loss.iloc[rsi_length] = loss.iloc[1:rsi_length + 1].mean()

    # 이후: Wilder 평활화 (RMA)
    for i in range(rsi_length + 1, len(close)):
        avg_gain.iloc[i] = (avg_gain.iloc[i - 1] * (rsi_length - 1) + gain.iloc[i]) / rsi_length
        avg_loss.iloc[i] = (avg_loss.iloc[i - 1] * (rsi_length - 1) + loss.iloc[i]) / rsi_length

    rs = avg_gain / avg_loss.replace(0, np.nan)
    rsi = 100 - (100 / (1 + rs))
    return rsi


# ===================== StochRSI 계산 =====================
# StochRSI = (RSI - RSI의 n봉 최솟값) / (RSI의 n봉 최댓값 - RSI의 n봉 최솟값)
# K = StochRSI의 smoothK봉 이동평균 * 100
# D = K의 smoothD봉 이동평균

def calculate_stoch_rsi(
    close: pd.Series,
    rsi_length: int = 14,
    stoch_length: int = 14,
    smooth_k: int = 3,
    smooth_d: int = 3
) -> pd.DataFrame:
    """
    Wilder RSI 기반 StochRSI 계산
    rsi_length  : RSI 계산 기간 (기본 14)
    stoch_length: StochRSI 룩백 기간 (기본 14)
    smooth_k    : K선 평활화 기간 (기본 3)
    smooth_d    : D선 평활화 기간 (기본 3)
    """
    rsi = calculate_wilder_rsi(close, rsi_length)

    rsi_min = rsi.rolling(window=stoch_length).min()
    rsi_max = rsi.rolling(window=stoch_length).max()
    rsi_range = rsi_max - rsi_min

    # 분모가 0이면 NaN 처리
    stoch_rsi = (rsi - rsi_min) / rsi_range.replace(0, np.nan)

    k = stoch_rsi.rolling(window=smooth_k).mean() * 100
    d = k.rolling(window=smooth_d).mean()

    return pd.DataFrame({
        'RSI_Wilder': rsi,
        'StochRSI_K': k,
        'StochRSI_D': d
    }, index=close.index)


# ===================== 계산 및 저장 =====================

print("RSI / StochRSI 계산 중...")
stoch_rsi_data = calculate_stoch_rsi(
    df['close'],
    rsi_length=14,
    stoch_length=14,
    smooth_k=3,
    smooth_d=3
)

result = pd.concat([df, stoch_rsi_data], axis=1)

output_path = "SOLUSDT_5years_15m_wilder.xlsx"
result.to_excel(output_path)

print(f"저장 완료: {output_path}")
print(f"Data shape : {result.shape}")
print(f"Date range : {result.index.min()} ~ {result.index.max()}")
print(result[['close', 'RSI_Wilder', 'StochRSI_K', 'StochRSI_D']].tail(10))