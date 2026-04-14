# 적용 내용
# 바이낸스 SOL/USDT 선물.
# 격리(Isolated) 마진.
# 레버리지 5배.
# 선물계좌 증거금의 50% 사용.
# 기존 SOL 포지션이 있으면 거래 안 함.

# 추세 전략 : MA18 4일 변화 추세 분석 (3일 연속 0.6% 이상 상승/하락 여부) 
# ㄴ 업비트 SOL 18일 MA가 3일 연속 0.6%이상 상승이면 숏 금지.
# ㄴ 업비트 SOL 18일 MA가 3일 연속 0.6%이상 하락이면 롱 금지.
# 지난 6일동안 같은 방향이고 변동성 0.4%이상이 5일이상 존재 상승/하락 추세로 보고 각각 숏/롱 진입 금지
# 현재가와 토요일 기준가 차이가 ±9% 이상이면 거래 금지. -> 위에 추세 전략에 해당이 되어서 빼도 되겠다.
# 업비트 기준 솔라나 시가가 어제는 43,18 위였는데, 오늘은 43,18 중 하나라도 아래면 롱 깨진 조건이니 롱 진입 금지
# 업비트 기준 솔라나 시가가 어제는 43,18 모두 위가 아니었는데, 오늘은 43,18 모두 위면 롱 진입 조건으로 숏 진입 금지
# 일,월,화,수,목 매일 1% TP룰
# while문으로 매일 9시에 거래 # 금요일/토요일 매매 금지.
# SOL 포지션이 있으면 금요일 종가에 close 하기, 가능하면 토요일 1시간봉 05:00봉 마감 06:00 에 close

# 적용 필요

import time
import datetime
import ccxt
import pyupbit
import pandas as pd
from datetime import timezone, timedelta

# KST 타임존 설정 및 전역 변수
KST = timezone(timedelta(hours=9))
SYMBOL = 'SOL/USDT'
UPBIT_TICKER = 'KRW-SOL'
MARKET_ID = 'SOLUSDT'
LEVERAGE = 5

# 바이낸스 선물 거래소 연결
exchange = ccxt.binance({
    'apiKey': 'QAK7GNH9rWZTCTaozqdNJOR9zsxB6N8QJieYRMDvXDt27ngVEwJs9tDOMAQsc1Bi',
    'secret': 'i8nNaQnZnsDL8gpAK7Q8yAWpxHZH9RYuHTY1q7ohMw9j1NXnmc1T6VCwetjfO48P',
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future',
    },
})

print("autotrade start")
# 현재 KST 시간 반환
def now_kst():
    return datetime.datetime.now(KST)
    
now = now_kst()
print(now) 

now = now_kst()
print(now) 

# 지난 토요일 06:00 바이낸스 SOL/USDT 종가 반환
def get_last_saturday_6_close():
    now = now_kst()
    sat6 = now.replace(hour=6, minute=0, second=0, microsecond=0)
    while sat6.weekday() != 5:
        sat6 -= datetime.timedelta(days=1)
    if now < sat6:
        sat6 -= datetime.timedelta(days=7)

    since_ms = int((sat6 - datetime.timedelta(days=7)).timestamp() * 1000)
    klines = exchange.fetch_ohlcv(SYMBOL, timeframe='1h', since=since_ms, limit=200)
    target_ms = int(sat6.astimezone(datetime.timezone.utc).timestamp() * 1000)

    for o in klines:
        if o[0] == target_ms:
            return float(o[4])
    raise ValueError("토요일 06:00 종가를 찾지 못했습니다.")

# SOL 포지션 보유 여부 확인
def has_sol_position():
    balance = exchange.fetch_balance(params={'type': 'future'})
    positions = balance.get('info', {}).get('positions', [])
    for p in positions:
        if p.get('symbol') == MARKET_ID and abs(float(p.get('positionAmt', 0))) > 0:
            return True
    return False

# 선물 계좌 USDT 사용 가능 잔고 반환
def get_available_usdt():
    balance = exchange.fetch_balance(params={'type': 'future'})
    return float(balance.get('free', {}).get('USDT', 0))

# Isolated 마진 모드 및 레버리지 설정
def set_margin_and_leverage():
    exchange.load_markets()
    exchange.set_margin_mode('isolated', SYMBOL)
    exchange.set_leverage(LEVERAGE, SYMBOL)

# 롱 포지션 TP 주문 생성 (MARK_PRICE 기준)
def place_tp_long(qty, tp_price):
    exchange.create_order(
        symbol=SYMBOL,
        type='TAKE_PROFIT_MARKET',
        side='sell',
        amount=qty,
        params={
            'stopPrice': tp_price,
            'closePosition': True,
            'workingType': 'MARK_PRICE'
        }
    )

# 숏 포지션 TP 주문 생성 (MARK_PRICE 기준)
def place_tp_short(qty, tp_price):
    exchange.create_order(
        symbol=SYMBOL,
        type='TAKE_PROFIT_MARKET',
        side='buy',
        amount=qty,
        params={
            'stopPrice': tp_price,
            'closePosition': True,
            'workingType': 'MARK_PRICE'
        }
    )

# 오늘 기준 업비트 SOL MA18, MA43 계산 (어제 종가 기준, 오늘 시가 비교용)
def get_upbit_ma18_ma43():
    df = pyupbit.get_ohlcv(UPBIT_TICKER, interval="day", count=60)
    if df is None or len(df) < 44:
        raise ValueError("업비트 일봉 데이터가 부족합니다.")

    df["ma18"] = df["close"].rolling(18).mean()
    df["ma43"] = df["close"].rolling(43).mean()

    prev = df.dropna().iloc[-2]
    return float(prev["ma18"]), float(prev["ma43"])

# 어제 기준 업비트 SOL MA18, MA43 계산 (그제 종가 기준, 어제 시가 비교용)
def get_upbit_yesterday_ma18_ma43():
    df = pyupbit.get_ohlcv(UPBIT_TICKER, interval="day", count=61)
    if df is None or len(df) < 45:
        raise ValueError("업비트 어제 MA 데이터 부족")
    
    df["ma18"] = df["close"].rolling(18).mean()
    df["ma43"] = df["close"].rolling(43).mean()
    
    yesterday = df.dropna().iloc[-2]
    return float(yesterday["ma18"]), float(yesterday["ma43"])

# 오늘 업비트 SOL 시가 반환
def get_upbit_today_open():
    df = pyupbit.get_ohlcv(UPBIT_TICKER, interval="day", count=3)
    if df is None or len(df) < 2:
        raise ValueError("업비트 오픈가 데이터를 가져오지 못했습니다.")
    return float(df.iloc[-1]["open"])

# 어제 업비트 SOL 시가 반환
def get_upbit_yesterday_open():
    df = pyupbit.get_ohlcv(UPBIT_TICKER, interval="day", count=3)
    if df is None or len(df) < 2:
        raise ValueError("업비트 어제 시가 데이터 부족")
    return float(df.iloc[-2]["open"])

# 업비트 SOL MA18 시리즈 반환 (추세 분석용)
def get_upbit_ma18_series():
    df = pyupbit.get_ohlcv(UPBIT_TICKER, interval="day", count=30)
    if df is None or len(df) < 18:
        raise ValueError("업비트 일봉 데이터가 부족합니다.")
    df["ma18"] = df["close"].rolling(18).mean()
    return df["ma18"].dropna()

# MA18 4일 변화 추세 분석 (3일 연속 0.6% 이상 상승/하락 여부)
def ma18_4day_change_trend():
    ma = get_upbit_ma18_series()
    last5 = ma.iloc[-5:].tolist()
    if len(last5) < 5:
        return None

    changes = []
    for i in range(1, 5):
        prev = last5[i - 1]
        cur = last5[i]
        change_pct = (cur / prev - 1) * 100
        changes.append(change_pct)

    up_3days = (
        changes[0] >= 0.6 and
        changes[1] >= 0.6 and
        changes[2] >= 0.6
    )

    down_3days = (
        changes[0] <= -0.6 and
        changes[1] <= -0.6 and
        changes[2] <= -0.6
    )

    return {
        "up_3days": up_3days,
        "down_3days": down_3days,
        "changes": changes,
        "last_ma18": last5[-1]
    }

# MA18 6일 연속 같은 방향 + 변동성 0.4%이상 5일이상 분석
def ma18_6day_volatility_trend():
    """
    지난 6일동안 MA18이 같은 방향으로 움직이고, 
    변동성이 0.4%이상인 날이 5일 이상이면 상승/하락 금지
    """
    ma = get_upbit_ma18_series()
    if len(ma) < 7:  # 최소 7개 데이터 필요 (6일 변화율 계산)
        return None

    last7 = ma.iloc[-7:].tolist()
    changes = []
    
    # 최근 6일 변화율 계산
    for i in range(1, 7):
        prev = last7[i - 1]
        cur = last7[i]
        change_pct = (cur / prev - 1) * 100  # +1.2%, -0.8% 등 방향성 포함
        changes.append(change_pct)

    # 같은 방향 확인 (모두 양수 or 모두 음수)
    all_up = all(c > 0 for c in changes)
    all_down = all(c < 0 for c in changes)
    
    # 변동성 0.4% 이상인 날 개수 (절댓값)
    high_vol_days = sum(abs(c) >= 0.4 for c in changes) # 절댓값으로 크기만 봄
    
    return {
        "all_up_6days": all_up,
        "all_down_6days": all_down,
        "high_vol_days": high_vol_days,
        "changes": changes,
        "last_ma18": last7[-1]
    }



# SOL 포지션 시장가 강제 종료 (토요일 06:00)
def close_sol_position():
    """토요일 06:00 SOL 포지션 시장가 강제 종료"""
    if not has_sol_position():
        print("종료할 SOL 포지션 없음")
        return False
    
    balance = exchange.fetch_balance(params={'type': 'future'})
    positions = balance.get('info', {}).get('positions', [])
    
    for p in positions:
        if p.get('symbol') == MARKET_ID:
            position_amt = float(p.get('positionAmt', 0))
            if abs(position_amt) > 0:
                side = 'sell' if position_amt > 0 else 'buy'
                exchange.create_market_order(SYMBOL, side, abs(position_amt))
                print(f"[토요일 06:00 자동 종료] SOL {side} | qty={abs(position_amt):.3f}")
                return True
    return False


# 메인 거래 로직 (매일 09:00 실행)
def trade_once():
    # 마진/레버리지 설정
    set_margin_and_leverage()

    now = now_kst()
    # 금/토 매매 금지
    if now.weekday() in [4, 5]:
        print("금요일/토요일은 매매 금지")
        return
    
    # 기존 포지션 확인
    if has_sol_position():
        print("기존 SOL 포지션이 있어서 거래하지 않음")
        return

    # 토요일 06:00 기준가 조회
    sat_close = get_last_saturday_6_close()
    current_price = float(exchange.fetch_ticker(SYMBOL)['last'])

    # # 토요일 기준가 ±9% 밖이면 매매 금지-추세 전략에 포함돼서 삭제
    # if current_price <= sat_close * 0.91 or current_price >= sat_close * 1.09:
    #     print("현재가와 토요일 기준가가 9% 이상 차이 나서 매매 금지")
    #     return

    # MA18 4일 추세 확인
    trend = ma18_4day_change_trend()
    if trend is None:
        print("MA18 추세 데이터를 가져오지 못했습니다.")
        return

    # ★ MA18 6일 변동성 추세 확인 (신규 추가) ★★★
    vol_trend = ma18_6day_volatility_trend()
    if vol_trend is None:
        print("MA18 6일 변동성 추세 데이터를 가져오지 못했습니다.")
        return


    # 오늘/어제 MA 및 시가 데이터 조회
    upbit_ma18, upbit_ma43 = get_upbit_ma18_ma43()
    yesterday_ma18, yesterday_ma43 = get_upbit_yesterday_ma18_ma43()
    upbit_today_open = get_upbit_today_open()
    upbit_yesterday_open = get_upbit_yesterday_open()

    # MA 위치 전환 룰 ★
    # 롱 금지: 어제 둘 다 위 → 오늘 하나라도 아래
    yesterday_above_both = (upbit_yesterday_open > yesterday_ma18 and upbit_yesterday_open > yesterday_ma43)
    today_below_either = (upbit_today_open < upbit_ma18 or upbit_today_open < upbit_ma43)

    # 숏 금지: 어제 둘 다 위가 아님(하나라도 아래) → 오늘 둘 다 위
    yesterday_not_above_both = (upbit_yesterday_open <= yesterday_ma18 or upbit_yesterday_open <= yesterday_ma43)
    today_above_both = (upbit_today_open > upbit_ma18 and upbit_today_open > upbit_ma43)

    # 주문 수량 계산 (사용 가능 USDT 50% * 레버리지)
    available_usdt = get_available_usdt()
    margin_to_use = available_usdt * 0.5
    notional = margin_to_use * LEVERAGE
    amount = round(notional / current_price, 3)

    if amount <= 0:
        print("주문 수량이 0이라서 중단")
        return

# # 기존 코드 (수정 전) 0=월,1=화,2=수,3=목,4=금,5=토,6=일
# 수요일/목요일 (weekday in [2, 3])	수,목	현재가 × 1.01 (+1%)	현재가 × 0.99 (-1%)
# 그 외 요일 (월,화,금,토,일)	나머지	sat_close (토요일 종가)	sat_close (토요일 종가)
#     weekday = now.weekday()
#     tp_price_long = current_price * 1.01 if weekday in [2, 3] else sat_close
#     tp_price_short = current_price * 0.99 if weekday in [2, 3] else sat_close


# 0.95% 익절룰로 수정
    tp_price_long = current_price * 1.0095
    tp_price_short = current_price * 0.9905
    
    # 디버그 정보 출력 (확장)
    print(f"[INFO] sat_close={sat_close}, current_price={current_price}")
    print(f"[UPBIT] today_open={upbit_today_open}, ma18={upbit_ma18}, ma43={upbit_ma43}")
    print(f"[YEST] yest_open={upbit_yesterday_open}, y_ma18={yesterday_ma18}, y_ma43={yesterday_ma43}")
    print(f"[TREND4] changes={trend['changes']}, up_3days={trend['up_3days']}, down_3days={trend['down_3days']}")
    print(f"[TREND6] all_up_6days={vol_trend['all_up_6days']}, all_down_6days={vol_trend['all_down_6days']}, high_vol_days={vol_trend['high_vol_days']}")
    now = now_kst()
    print(now) 
    
    # 롱 진입 조건
    if current_price <= sat_close * 0.99:
        # 기존 3일 연속 하락 금지        
        if trend["down_3days"]:
            print("3일 연속 0.6% 이상 하락이라 롱 진입 금지")
            return

        # ★신규: 6일 연속 하락 + 변동성 0.4%이상 5일이상 금지 ★★★
        if vol_trend["all_down_6days"] and vol_trend["high_vol_days"] >= 5:
            print("6일 연속 하락 + 변동성 0.4%이상 5일이상 → 롱 진입 금지")
            return

        # 롱 금지: 어제 MA위(OR) → 오늘 MA아래(OR)
        if yesterday_above_both and today_below_either:
            print("어제 MA위→오늘 MA아래 전환으로 롱 진입 금지")
            return

        # 롱 진입
        exchange.create_market_buy_order(SYMBOL, amount)
        place_tp_long(amount, tp_price_long)
        print(f"롱 진입 | amount={amount} | price={current_price} | tp={tp_price_long}")





    # 숏 진입 조건
    elif current_price >= sat_close * 1.01:
        # 기존 3일 연속 상승 금지
        if trend["up_3days"]:
            print("3일 연속 0.5% 이상 상승이라 숏 진입 금지")
            return

        # ★ 신규: 6일 연속 상승 + 변동성 0.4%이상 5일이상 금지
        if vol_trend["all_up_6days"] and vol_trend["high_vol_days"] >= 5:
            print("6일 연속 상승 + 변동성 0.4%이상 5일이상 → 숏 진입 금지")
            return

        # 숏 금지: 어제 MA아래(OR) → 오늘 MA위(OR)
        if yesterday_not_above_both and today_above_both:
            print("어제 MA아래→오늘 MA위 전환으로 숏 진입 금지")
            return
        
        # 숏 진입
        exchange.create_market_sell_order(SYMBOL, amount)
        place_tp_short(amount, tp_price_short)
        print(f"숏 진입 | amount={amount} | price={current_price} | tp={tp_price_short}")

    else:
        print("진입 조건 없음")
        
# 메인 루프 제어 변수 (그대로 유지)
last_run_date = None

# 무한 루프: 매 1초마다 조건 확인
while True:
    try:
        now = now_kst()


        # ★★★ 토요일 06:00 포지션 강제 종료 (유지)
        if now.weekday() == 5 and now.hour == 6 and now.minute == 0:
            print("=== 토요일 06:00 포지션 종료 ===")
            close_sol_position()


        # *******************************************************************
        # ☆☆☆ 09:00 KST에 그날 한 번만 진입 ☆☆☆
        if now.hour == 21 and now.minute == 12:
            if last_run_date != now.date():
                if not has_sol_position():  # 이 줄은 유지해도 됨 (선택)
                    trade_once()
                    last_run_date = now.date()


        time.sleep(1)   # 1초마다 스캔 ( 유지 )

    except Exception as e:
        print(e)
        time.sleep(10)

