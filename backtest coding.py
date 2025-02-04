import pyupbit
import pandas as pd

def get_historical_data(ticker, days):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=days)
    return df

def calculate_rsi(series, period=14):
    delta = series.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def backtest_strategy(df):
    df['MA20'] = df['close'].rolling(window=20).mean()
    df['MA30'] = df['close'].rolling(window=30).mean()
    df['RSI'] = calculate_rsi(df['close'], 14)
    
    df['Signal'] = 0
    df.loc[(df['close'] > df['MA20']) & (df['close'] > df['MA30']) & (df['RSI'] < 30), 'Signal'] = 1
    
    df['Returns'] = df['close'].pct_change()
    df['Strategy_Returns'] = df['Signal'].shift(1) * df['Returns']
    
    return df

# 데이터 가져오기
ticker = "KRW-BTC"
days = 365 * 3  # 3년치 데이터
df = get_historical_data(ticker, days)

# 백테스트 수행
result = backtest_strategy(df)

# 결과 출력
cumulative_returns = (1 + result['Strategy_Returns']).cumprod().fillna(1)
total_return = cumulative_returns.iloc[-1] - 1
print(f"총 수익률: {total_return:.2%}")