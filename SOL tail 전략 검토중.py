
#7 ==========5m봉 급락시 진입 전략========

def analyze_volume_spike_drop(
    symbol,
    timeframe,
    side,  # 'long' or 'short'
    df=None
):
    """
    거래량 폭발 급락/급등 룰

    - side='long': 급락 후 반등 (롱)
    - side='short': 급등 후 하락 (숏)

    기본 조건:
    1) 직전봉의 직전 8 개봉 [-9:-1] 중 range_volatility > 1% (롱) / 1.5% (숏)
    2) 롱: 직전 8 개봉의 마지막 봉 종가가 range_high 보다 -1% 이상 낮음
       숏: 직전 8 개봉의 마지막 봉 종가가 range_low 보다 +1.5% 이상 높음
    3) 직전봉의 직전 4 개봉 [-5:-1] 거래량 평균보다
       직전봉 거래량이 3 배 (롱) / 4 배 (숏) 이상
    4) 직전봉 거래량이 120k 이상 (절대적 기준)
    5) 직전봉 거래량이 지난 4 개봉 평균의 10 배 미만 (과도한 거래량 필터)

    예외 조건 (롱 전용):
    - range_volatility 는 만족하지만 거래량 조건 불만족일 때
      아래 두 가지 중 하나를 만족하면 2 배 또는 1.5 배만 요구

    예외 1:
    - [-9:-1] 구간에서
      * 음봉 개수 >= 7
      * 음봉 중 꼬리가 몸통의 1/3 이상인 캔들 >= 3
    → 직전 3 개봉 [-4:-1] 거래량 평균의 2 배 이상이면 OK

    예외 2:
    - [-9:] 구간 (직전봉 포함 9 개봉) 에서
      * 변동성 >= 0.5% 인 음봉 >= 2
      * 변동성 >= 0.35% 인 음봉 >= 3
      * 그중 꼬리가 몸통의 1/3 이상인 캔들 >= 2
    → 직전 3 개봉 [-4:-1] 거래량 평균의 1.5 배 이상이면 OK

    예외 조건 3, 4, 5 (롱/숏 공통):
    - 공통 조건 1:
      * 롱: 직전 12 개봉 중 (직전 11 개봉 low)*1.001 < 직전봉 종가
      * 숏: 직전 12 개봉 중 (직전 11 개봉 high)*0.999 > 직전봉 종가
    - 공통 조건 2: 캔들 변동성 0.1% 이상인데 꼬리가 0.4% 이상
      * 꼬리 2 개 또는 0.4% 캔들 1 개로 취급

    - 진입 예외 조건 3: 캔들 변동성 0.3% 이상 3 개, 0.4% 이상 1 개 + 꼬리 2 개 이상
    - 진입 예외 조건 4: 0.2% 3 개 이상, 0.5% 2 개 이상 + 꼬리 2 개 이상
    - 진입 예외 조건 5: 0.5% 3 개이상 + 0.4% 4 개이상 이면 꼬리 1 개로 진입 가능

    15 분 전략룰:
    - 공통 조건 1:
      * 롱: 직전 12 개봉 중 (직전 11 개봉 low)*1.001 < 직전봉 종가
      * 숏: 직전 12 개봉 중 (직전 11 개봉 high)*0.999 > 직전봉 종가
    - 공통 조건 2: 캔들 변동성 0.1% 이상인데 꼬리가 0.4% 이상
      * 꼬리 2 개, 0.4% 캔들 1 개 취급
      * 추가적으로 0.15% 3 개 이상이면 1/3 꼬리 1 개, 0.4% 봉 1 개로 취급

    - 15 분 예외 1: 0.4% 3 개 이상, 꼬리 2 개 이상
    - 15 분 예외 2: 0.15% 4 개 이상, 0.3% 2 개 이상, 꼬리 2 개 이상
    - 꼬리는 각 조건의 변동성 기준이 되는 캔들에 대해서만 적용
    """

    if df is None:
        df = get_confirmed_candles_with_rsi(symbol, timeframe)

    if df is None or len(df) < 12:
        return None

    prev = df.iloc[-1]  # 직전봉

    # 구간 정의
    last_8_ex_prev = df.iloc[-9:-1]  # 직전봉의 직전 8 개봉
    last_4_ex_prev = df.iloc[-5:-1]  # 직전봉의 직전 4 개봉
    last_3_ex_prev = df.iloc[-4:-1]  # 직전봉의 직전 3 개봉
    last_9_incl_prev = df.iloc[-9:]  # 직전봉 포함 9 개봉
    last_12_incl_prev = df.iloc[-12:]  # 직전봉 포함 12 개봉
    last_11_ex_prev = df.iloc[-12:-1]  # 직전봉의 직전 11 개봉

    # -------------------------------------------------
    # 1) range_volatility 계산 (직전봉의 직전 8 개봉)
    # -------------------------------------------------
    range_high = last_8_ex_prev['close'].max()
    range_low = last_8_ex_prev['close'].min()

    if range_high == 0:
        return None

    range_volatility = (range_high - range_low) / range_high

    # -------------------------------------------------
    # 2) 방향별 추가 조건 (롱: -1%, 숏: +1.5%)
    # -------------------------------------------------
    # 직전 8 개봉의 마지막 봉 (인덱스 -2)
    last_of_8_close = last_8_ex_prev.iloc[-1]['close']

    if side == 'long':
        # 롱: 마지막 봉 종가가 range_high 보다 -1% 이상 낮음
        cond_direction = last_of_8_close <= range_high * (1 - 0.01)
    else:
        # 숏: 마지막 봉 종가가 range_low 보다 +1.5% 이상 높음
        cond_direction = last_of_8_close >= range_low * (1 + 0.015)

    # 사이드별 임계치
    if side == 'long':
        range_vol_threshold = 0.01
        vol_mult_base = 3.0
        vol_mult_exc1 = 2.0
        vol_mult_exc2 = 1.5
    else:  # short
        range_vol_threshold = 0.01
        vol_mult_base = 3.0
        vol_mult_exc1 = None  # 숏은 예외 조건 없음
        vol_mult_exc2 = None

    # range_volatility 조건 AND 방향 조건
    cond_range_vol = range_volatility >= range_vol_threshold
    cond_range_and_direction = cond_range_vol and cond_direction

    if not cond_range_and_direction:
        reason = "range_volatility 부족" if not cond_range_vol else "방향 조건 불만족"
        return {
            "signal": False,
            "side": side,
            "reason": reason,
            "range_volatility": float(range_volatility),
            "last_of_8_close": float(last_of_8_close),
            "range_high": float(range_high),
            "range_low": float(range_low),
            "cond_direction": cond_direction,
        }

    # -------------------------------------------------
    # 3) 거래량 조건 (기본 룰)
    # -------------------------------------------------
    avg_vol_4 = last_4_ex_prev['volume'].mean()

    if avg_vol_4 == 0:
        return None

    vol_ratio = prev['volume'] / avg_vol_4

    # 절대적 거래량 기준: 120k 이상
    abs_vol_threshold = 120_000
    cond_abs_vol = prev['volume'] >= abs_vol_threshold

    # 과도한 거래량 필터: 10 배 이상이면 진입 금지
    max_vol_ratio = 10.0
    cond_max_vol = vol_ratio < max_vol_ratio

    cond_vol_base = vol_ratio >= vol_mult_base

    # 거래량 조건: 배수 조건 AND 절대적 기준 AND 과도한 거래량 필터
    cond_vol_base = cond_vol_base and cond_abs_vol and cond_max_vol

    # -------------------------------------------------
    # 4) 롱일 때만 예외 조건 처리 (기존 exc1, exc2)
    # -------------------------------------------------
    cond_exc1 = False
    cond_exc2 = False

    if side == 'long' and not cond_vol_base:
        # -------------------------
        # 예외 조건 1
        # -------------------------
        # [-9:-1] 구간에서 음봉 개수 >= 7
        # 음봉 중 꼬리가 몸통의 1/3 이상인 캔들 >= 3

        # 음봉: close < open
        bearish_8 = last_8_ex_prev[
            last_8_ex_prev['close'] < last_8_ex_prev['open']
        ]

        cond_exc1_bearish_count = len(bearish_8) >= 7

        # 몸통 = open - close
        # 꼬리 = close - low
        # 꼬리 / 몸통 >= 1/3
        if len(bearish_8) > 0:
            body_8 = bearish_8['open'] - bearish_8['close']
            tail_8 = bearish_8['close'] - bearish_8['low']

            # body 가 0 이면 division by zero 방지
            ratio_8 = tail_8 / body_8.replace(0, np.nan)
            long_tail_8 = (ratio_8 >= 1.0 / 3.0).sum()
        else:
            long_tail_8 = 0

        cond_exc1_long_tail = long_tail_8 >= 3

        cond_exc1 = (
            cond_exc1_bearish_count
            and cond_exc1_long_tail
        )

        # 예외 1 이 만족되면 거래량 배수 2.0 으로 완화 (절대적 기준과 과도한 거래량 필터는 유지)
        if cond_exc1:
            cond_vol_base = (vol_ratio >= vol_mult_exc1) and cond_abs_vol and cond_max_vol

        # -------------------------
        # 예외 조건 2 (예외 1 이 만족 안 됐을 때만 체크)
        # -------------------------
        if not cond_exc1:
            # [-9:] 구간 (직전봉 포함 9 개봉)
            # 변동성 >= 0.5% 음봉 >= 2
            # 변동성 >= 0.35% 음봉 >= 3
            # 그중 꼬리가 몸통의 1/3 이상인 캔들 >= 2

            # 변동성 = (open - close) / open
            vola_9 = (
                (last_9_incl_prev['open'] - last_9_incl_prev['close'])
                / last_9_incl_prev['open']
            )

            bearish_9 = last_9_incl_prev[
                last_9_incl_prev['close'] < last_9_incl_prev['open']
            ]

            if len(bearish_9) > 0:
                vola_bearish_9 = (
                    (bearish_9['open'] - bearish_9['close'])
                    / bearish_9['open']
                )

                cond_vol_05 = (vola_bearish_9 >= 0.005).sum() >= 2
                cond_vol_035 = (vola_bearish_9 >= 0.0035).sum() >= 3
            else:
                cond_vol_05 = False
                cond_vol_035 = False

            # 꼬리 / 몸통 >= 1/3 인 캔들 개수
            if len(bearish_9) > 0:
                body_9 = bearish_9['open'] - bearish_9['close']
                tail_9 = bearish_9['close'] - bearish_9['low']

                ratio_9 = tail_9 / body_9.replace(0, np.nan)
                long_tail_9 = (ratio_9 >= 1.0 / 3.0).sum()
            else:
                long_tail_9 = 0

            cond_exc2_long_tail = long_tail_9 >= 2

            cond_exc2 = (
                cond_vol_05
                and cond_vol_035
                and cond_exc2_long_tail
            )

            # 예외 2 가 만족되면 거래량 배수 1.5 로 완화 (절대적 기준과 과도한 거래량 필터는 유지)
            if cond_exc2:
                cond_vol_base = (vol_ratio >= vol_mult_exc2) and cond_abs_vol and cond_max_vol

    # -------------------------------------------------
    # 5) 예외 조건 3, 4, 5 (롱/숏 공통, 기존과 독립적)
    # -------------------------------------------------
    cond_exc3 = False
    cond_exc4 = False
    cond_exc5 = False

    # -------------------------------------------------
    # 6) 15m 전용 예외 조건 (롱/숏 공통)
    # -------------------------------------------------
    cond_15m_common1 = False
    cond_15m_common2 = False
    cond_15m_extra_tail_rule = False
    cond_15m_exc1 = False
    cond_15m_exc2 = False

    if not cond_vol_base:
        # 공통 조건 1: 직전 12 개봉 중 (직전 11 개봉 high/low) 기준
        if side == 'long':
            # ✅ 롱: (직전 11 개봉 low)*1.001 < 직전봉 종가
            min_low_11 = last_11_ex_prev['low'].min()
            cond_common1 = prev['close'] < min_low_11 * 1.001
        else:
            # 숏: (직전 11 개봉 high)*0.999 > 직전봉 종가
            max_high_11 = last_11_ex_prev['high'].max()
            cond_common1 = prev['close'] > max_high_11 * 0.999
        
        # 공통 조건 2: 캔들 변동성 0.1% 이상인데 꼬리가 0.4% 이상
        # ✅ 롱: 음봉의 아래꼬리 (close - low)
        # ✅ 숏: 양봉의 윗꼬리 (high - close)
        # 몸통: abs(open - close)
        
        # 직전 12 개봉 중 변동성 0.1% 이상인 캔들 필터
        candles_12 = last_12_incl_prev
        body_12 = abs(candles_12['open'] - candles_12['close'])
        volatility_12 = body_12 / candles_12['open']
        
        # 변동성 0.1% 이상인 캔들만 필터
        cond_vol_01 = volatility_12 >= 0.001
        
        if side == 'long':
            # ✅ 롱: 음봉만 (close < open)
            cond_bearish = candles_12['close'] < candles_12['open']
            # ✅ 롱: 아래꼬리 = close - low
            tail_12 = candles_12['close'] - candles_12['low']
        else:
            # ✅ 숏: 양봉만 (close > open)
            cond_bearish = candles_12['close'] > candles_12['open']
            # ✅ 숏: 윗꼬리 = high - close
            tail_12 = candles_12['high'] - candles_12['close']
        
        tail_ratio_12 = tail_12 / body_12.replace(0, np.nan)
        cond_tail_04 = tail_ratio_12 >= (0.004 / candles_12['open'])  # 0.4% 절대값
        
        # 꼬리 2 개 또는 0.4% 캔들 1 개로 취급
        # 꼬리 개수: 변동성 0.1% 이상 + 꼬리 0.4% 이상
        tail_count = (cond_vol_01 & cond_tail_04 & cond_bearish).sum()
        
        # 0.4% 캔들 1 개: 변동성 0.1% 이상 + 꼬리 0.4% 이상인 캔들 중 1 개
        cond_common2 = tail_count >= 2 or (tail_count >= 1 and (cond_vol_01 & cond_tail_04 & cond_bearish).any())
        
        # 공통 조건 1 AND 공통 조건 2
        cond_common = cond_common1 and cond_common2
        
        if cond_common:
            # ✅ 롱: 음봉 변동성, 숏: 양봉 변동성
            if side == 'long':
                # ✅ 롱: 음봉만 (close < open)
                bearish_candles_12 = candles_12[candles_12['close'] < candles_12['open']]
                if len(bearish_candles_12) > 0:
                    vola_bearish_12 = (
                        (bearish_candles_12['open'] - bearish_candles_12['close'])
                        / bearish_candles_12['open']
                    )
                    body_bearish_12 = bearish_candles_12['open'] - bearish_candles_12['close']
                    tail_bearish_12 = bearish_candles_12['close'] - bearish_candles_12['low']
                    tail_ratio_bearish_12 = tail_bearish_12 / body_bearish_12.replace(0, np.nan)
                else:
                    vola_bearish_12 = pd.Series(dtype='float64')
                    tail_ratio_bearish_12 = pd.Series(dtype='float64')
            else:
                # ✅ 숏: 양봉만 (close > open)
                bullish_candles_12 = candles_12[candles_12['close'] > candles_12['open']]
                if len(bullish_candles_12) > 0:
                    vola_bullish_12 = (
                        (bullish_candles_12['close'] - bullish_candles_12['open'])
                        / bullish_candles_12['open']
                    )
                    body_bullish_12 = bullish_candles_12['close'] - bullish_candles_12['open']
                    tail_bullish_12 = bullish_candles_12['high'] - bullish_candles_12['close']
                    tail_ratio_bullish_12 = tail_bullish_12 / body_bullish_12.replace(0, np.nan)
                else:
                    vola_bullish_12 = pd.Series(dtype='float64')
                    tail_ratio_bullish_12 = pd.Series(dtype='float64')
            
            if side == 'long':
                # 진입 예외 조건 3: 캔들 변동성 0.3% 이상 3 개, 0.4% 이상 1 개 + 꼬리 2 개 이상
                cond_vol_03 = (vola_bearish_12 >= 0.003).sum() >= 3
                cond_vol_04 = (vola_bearish_12 >= 0.004).sum() >= 1
                # ✅ 꼬리 1/3 이상인 캔들만 카운트 (변동성 0.3% 이상 또는 0.4% 이상인 캔들 중)
                cond_vol_03_04 = (vola_bearish_12 >= 0.003) | (vola_bearish_12 >= 0.004)
                cond_tail_1_3 = (tail_ratio_bearish_12 >= 1.0 / 3.0) & cond_vol_03_04
                cond_tail_2 = cond_tail_1_3.sum() >= 2
                
                cond_exc3 = cond_vol_03 and cond_vol_04 and cond_tail_2
                
                # 진입 예외 조건 4: 0.2% 3 개 이상, 0.5% 2 개 이상 + 꼬리 2 개 이상
                cond_vol_02 = (vola_bearish_12 >= 0.002).sum() >= 3
                cond_vol_05 = (vola_bearish_12 >= 0.005).sum() >= 2
                # ✅ 꼬리 1/3 이상인 캔들만 카운트 (변동성 0.2% 이상 또는 0.5% 이상인 캔들 중)
                cond_vol_02_05 = (vola_bearish_12 >= 0.002) | (vola_bearish_12 >= 0.005)
                cond_tail_1_3_v2 = (tail_ratio_bearish_12 >= 1.0 / 3.0) & cond_vol_02_05
                cond_tail_2_v2 = cond_tail_1_3_v2.sum() >= 2
                
                cond_exc4 = cond_vol_02 and cond_vol_05 and cond_tail_2_v2
                
                # 진입 예외 조건 5: 0.5% 3 개이상 + 0.4% 4 개이상 이면 꼬리 1 개로 진입 가능
                cond_vol_05_v2 = (vola_bearish_12 >= 0.005).sum() >= 3
                cond_vol_04_v2 = (vola_bearish_12 >= 0.004).sum() >= 4
                # ✅ 꼬리 1/3 이상인 캔들만 카운트 (변동성 0.5% 이상 또는 0.4% 이상인 캔들 중)
                cond_vol_05_04 = (vola_bearish_12 >= 0.005) | (vola_bearish_12 >= 0.004)
                cond_tail_1_3_v3 = (tail_ratio_bearish_12 >= 1.0 / 3.0) & cond_vol_05_04
                cond_tail_1 = cond_tail_1_3_v3.sum() >= 1
                
                cond_exc5 = cond_vol_05_v2 and cond_vol_04_v2 and cond_tail_1
            else:
                # ✅ 숏: 양봉 변동성
                cond_vol_03 = (vola_bullish_12 >= 0.003).sum() >= 3
                cond_vol_04 = (vola_bullish_12 >= 0.004).sum() >= 1
                # ✅ 꼬리 1/3 이상인 캔들만 카운트 (변동성 0.3% 이상 또는 0.4% 이상인 캔들 중)
                cond_vol_03_04 = (vola_bullish_12 >= 0.003) | (vola_bullish_12 >= 0.004)
                cond_tail_1_3 = (tail_ratio_bullish_12 >= 1.0 / 3.0) & cond_vol_03_04
                cond_tail_2 = cond_tail_1_3.sum() >= 2
                
                cond_exc3 = cond_vol_03 and cond_vol_04 and cond_tail_2
                
                cond_vol_02 = (vola_bullish_12 >= 0.002).sum() >= 3
                cond_vol_05 = (vola_bullish_12 >= 0.005).sum() >= 2
                # ✅ 꼬리 1/3 이상인 캔들만 카운트 (변동성 0.2% 이상 또는 0.5% 이상인 캔들 중)
                cond_vol_02_05 = (vola_bullish_12 >= 0.002) | (vola_bullish_12 >= 0.005)
                cond_tail_1_3_v2 = (tail_ratio_bullish_12 >= 1.0 / 3.0) & cond_vol_02_05
                cond_tail_2_v2 = cond_tail_1_3_v2.sum() >= 2
                
                cond_exc4 = cond_vol_02 and cond_vol_05 and cond_tail_2_v2
                
                cond_vol_05_v2 = (vola_bullish_12 >= 0.005).sum() >= 3
                cond_vol_04_v2 = (vola_bullish_12 >= 0.004).sum() >= 4
                # ✅ 꼬리 1/3 이상인 캔들만 카운트 (변동성 0.5% 이상 또는 0.4% 이상인 캔들 중)
                cond_vol_05_04 = (vola_bullish_12 >= 0.005) | (vola_bullish_12 >= 0.004)
                cond_tail_1_3_v3 = (tail_ratio_bullish_12 >= 1.0 / 3.0) & cond_vol_05_04
                cond_tail_1 = cond_tail_1_3_v3.sum() >= 1
                
                cond_exc5 = cond_vol_05_v2 and cond_vol_04_v2 and cond_tail_1
            
            # ✅ 예외 조건 3, 4, 5 중 하나라도 만족하면 거래량 조건 없이 바로 진입
            if cond_exc3 or cond_exc4 or cond_exc5:
                cond_vol_base = True
        
        # -------------------------------------------------
        # 15m 전용 예외 조건
        # -------------------------------------------------
        if timeframe == '15m' and cond_common:
            # 15m 공통 조건 1
            cond_15m_common1 = cond_common1
            
            # 15m 공통 조건 2: 캔들 변동성 0.1% 이상인데 꼬리가 0.4% 이상
            # 꼬리 2 개 또는 0.4% 캔들 1 개로 취급
            cond_15m_common2 = cond_common2
            
            # 추가 규칙: 0.15% 3 개 이상이면 1/3 꼬리 1 개, 0.4% 봉 1 개로 취급
            if side == 'long':
                tail_on_015 = (vola_bearish_12 >= 0.0015) & (tail_ratio_bearish_12 >= 1.0 / 3.0)
                cond_15m_extra_tail_rule = (
                    (vola_bearish_12 >= 0.0015).sum() >= 3
                    and tail_on_015.sum() >= 1
                )
            else:
                tail_on_015 = (vola_bullish_12 >= 0.0015) & (tail_ratio_bullish_12 >= 1.0 / 3.0)
                cond_15m_extra_tail_rule = (
                    (vola_bullish_12 >= 0.0015).sum() >= 3
                    and tail_on_015.sum() >= 1
                )
            
            # 15m 예외 1: 0.4% 3 개 이상, 꼬리 2 개 이상
            if side == 'long':
                candles_vol_04 = vola_bearish_12 >= 0.004
                tail_on_04 = candles_vol_04 & (tail_ratio_bearish_12 >= 1.0 / 3.0)
                cond_15m_exc1 = (
                    (vola_bearish_12 >= 0.004).sum() >= 3
                    and tail_on_04.sum() >= 2
                )
            else:
                candles_vol_04 = vola_bullish_12 >= 0.004
                tail_on_04 = candles_vol_04 & (tail_ratio_bullish_12 >= 1.0 / 3.0)
                cond_15m_exc1 = (
                    (vola_bullish_12 >= 0.004).sum() >= 3
                    and tail_on_04.sum() >= 2
                )
            
            # 15m 예외 2: 0.15% 4 개 이상, 0.3% 2 개 이상, 꼬리 2 개 이상
            if side == 'long':
                candles_vol_015 = vola_bearish_12 >= 0.0015
                candles_vol_03 = vola_bearish_12 >= 0.003
                tail_on_015 = candles_vol_015 & (tail_ratio_bearish_12 >= 1.0 / 3.0)
                cond_15m_exc2 = (
                    candles_vol_015.sum() >= 4
                    and candles_vol_03.sum() >= 2
                    and tail_on_015.sum() >= 2
                )
            else:
                candles_vol_015 = vola_bullish_12 >= 0.0015
                candles_vol_03 = vola_bullish_12 >= 0.003
                tail_on_015 = candles_vol_015 & (tail_ratio_bullish_12 >= 1.0 / 3.0)
                cond_15m_exc2 = (
                    candles_vol_015.sum() >= 4
                    and candles_vol_03.sum() >= 2
                    and tail_on_015.sum() >= 2
                )
            
            # 15m 예외 1 또는 2 는 거래량 조건 없이 진입 가능
            if cond_15m_exc1 or cond_15m_exc2:
                cond_vol_base = True

    # 최종 시그널
    signal = cond_range_and_direction and cond_vol_base

    return {
        "signal": signal,
        "side": side,

        "range_volatility": float(range_volatility),
        "range_vol_threshold": float(range_vol_threshold),

        "avg_vol_4": float(avg_vol_4),
        "prev_volume": float(prev['volume']),
        "vol_ratio": float(vol_ratio),
        "abs_volume": float(prev['volume']),
        "abs_volume_threshold": abs_vol_threshold,
        "cond_abs_volume": cond_abs_vol,
        "max_vol_ratio": max_vol_ratio,
        "cond_max_volume": cond_max_vol,
        "vol_mult_required": (
            vol_mult_base
            if cond_vol_base and (side == 'short' or (cond_exc1 is False and cond_exc2 is False and cond_exc3 is False and cond_exc4 is False and cond_exc5 is False))
            else (
                vol_mult_exc1 if cond_exc1 else (vol_mult_exc2 if cond_exc2 else 2.0)
            )
        ),

        "cond_range_vol": cond_range_vol,
        "cond_direction": cond_direction,
        "cond_vol_base": cond_vol_base,

        # 롱 전용 예외 조건 정보
        "cond_exc1": cond_exc1 if side == 'long' else None,
        "cond_exc2": cond_exc2 if side == 'long' else None,
        
        # 롱/숏 공통 예외 조건 정보
        "cond_exc3": cond_exc3,
        "cond_exc4": cond_exc4,
        "cond_exc5": cond_exc5,
        "cond_common1": cond_common1 if (cond_exc3 or cond_exc4 or cond_exc5) else None,
        "cond_common2": cond_common2 if (cond_exc3 or cond_exc4 or cond_exc5) else None,
        
        # 15m 전용 예외 조건 정보
        "cond_15m_common1": cond_15m_common1,
        "cond_15m_common2": cond_15m_common2,
        "cond_15m_extra_tail_rule": cond_15m_extra_tail_rule,
        "cond_15m_exc1": cond_15m_exc1,
        "cond_15m_exc2": cond_15m_exc2,

        # 직전봉 정보
        "prev_open": float(prev['open']),
        "prev_close": float(prev['close']),
        "prev_low": float(prev['low']),
        "prev_high": float(prev['high']),
        "prev_volume": float(prev['volume']),

        "tp_price": float(prev['close']) * (1 + (0.01 if side == 'long' else -0.01)),
        "sl_price": float(prev['close']) * (1 - (0.007 if side == 'long' else -0.007))
    }
  
# 5,15분봉 3틱& 거래량 급등 롱   
    
# def trade_rsi_close_strategy_link(
#     symbol,
#     market_id,
#     timeframe,
#     side,
#     tp_pct_1,
#     tp_pct_2=None,
#     min_volatility=0.003,
#     price_diff_pct=0.001,
#     rsi_raise_pct=0.003,
#     rsi_drop_pct=0.003,
#     min_range_volatility=0.015
# ):
#     global last_link_long_trade_time, last_link_short_trade_time
#     global last_link_long_5m, last_link_short_5m
#     global last_link_long_15m, last_link_short_15m

#     now = time.time()

#     if side == 'long':
#         if now - last_link_long_trade_time < 60:
#             print(f"[{symbol} LINK_LONG] 60 초 쿨다운 중 진입 금지")
#             return
#         if timeframe == '5m' and now - last_link_long_5m < 400:
#             minutes_ago = (now - last_link_long_5m) / 60
#             print(f"[{symbol} LINK_LONG 5m] 최근 {minutes_ago:.1f}분 전에 매수됨 (6 분 내 중복매수 금지)")
#             return
#         if timeframe == '15m' and now - last_link_long_15m < 900:
#             minutes_ago = (now - last_link_long_15m) / 60
#             print(f"[{symbol} LINK_LONG 15m] 최근 {minutes_ago:.1f}분 전에 매수됨 (15 분 내 중복매수 금지)")
#             return
#     else:
#         if now - last_link_short_trade_time < 60:
#             print(f"[{symbol} LINK_SHORT] 60 초 쿨다운 중 진입 금지")
#             return
#         if timeframe == '5m' and now - last_link_short_5m < 400:
#             minutes_ago = (now - last_link_short_5m) / 60
#             print(f"[{symbol} LINK_SHORT 5m] 최근 {minutes_ago:.1f}분 전에 매도됨 (6 분 내 중복매도 금지)")
#             return
#         if timeframe == '15m' and now - last_link_short_15m < 900:
#             minutes_ago = (now - last_link_short_15m) / 60
#             print(f"[{symbol} LINK_SHORT 15m] 최근 {minutes_ago:.1f}분 전에 매도됨 (15 분 내 중복매도 금지)")
#             return

#     set_margin_and_leverage(symbol)
#     current_balance = get_available_usdt()

#     if current_balance < 2500 or current_balance > 12000:
#         print(f"[{symbol}] 계좌 잔고 {current_balance:.2f} USD 범위 밖이므로 진입 금지")
#         return

#     link_position = get_position_amount('LINK/USDT')
#     sol_position = get_position_amount('SOL/USDT')

#     if side == 'long':
#         if link_position <= 0:
#             print(f"[{symbol} LINK_LONG] LINK 롱 포지션 없음")
#             return
#         n_link = abs(link_position)
#         sol_threshold = 60 * n_link
#         current_sol = sol_position if sol_position > 0 else 0
#         print(f"[{symbol} LINK_LONG] LINK={n_link}, SOL롱={current_sol}, 기준={sol_threshold}")
#         if current_sol > sol_threshold:
#             print(f"[{symbol} LINK_LONG] SOL 롱 보유량이 기준 초과")
#             return
#     else:
#         if link_position >= 0:
#             print(f"[{symbol} LINK_SHORT] LINK 숏 포지션 없음")
#             return
#         n_link = abs(link_position)
#         sol_threshold = 60 * n_link
#         current_sol = -sol_position if sol_position < 0 else 0
#         print(f"[{symbol} LINK_SHORT] LINK={n_link}, SOL숏={current_sol}, 기준={sol_threshold}")
#         if current_sol > sol_threshold:
#             print(f"[{symbol} LINK_SHORT] SOL 숏 보유량이 기준 초과")
#             return

#     current_price = float(exchange.fetch_ticker(symbol)['last'])
#     available_usdt = get_available_usdt()
#     margin_to_use = available_usdt * 0.5
#     notional = margin_to_use * LEVERAGE
#     amount = round(notional / current_price, 3)

#     if amount <= 0:
#         print(f"[{symbol}] 주문 수량이 0 이라서 중단")
#         return

#     # -------------------------------------------------
#     # 거래량 폭발 신호 (롱)
#     # -------------------------------------------------
#     if side == 'long':
#         vol_signal = analyze_volume_spike_drop(
#             symbol=symbol,
#             timeframe=timeframe,
#             side='long'
#         )

#         print(f"[{symbol} LINK_LONG] VOLUME_SPIKE={vol_signal}")

#         if not vol_signal or not vol_signal["signal"]:
#             print(f"[{symbol} LINK_LONG] 거래량 폭발 조건 불만족으로 진입 금지")
#             return

#         tp_pct = tp_pct_2 if (tp_pct_2 is not None and vol_signal["range_volatility"] > 0.018) else tp_pct_1
#         tp_price = vol_signal["prev_close"] * (1 + tp_pct)
#         sl_price = vol_signal["prev_close"] * (1 - 0.035)

#         exchange.create_market_buy_order(symbol, amount)

#         last_link_long_trade_time = time.time()
#         if timeframe == '5m':
#             last_link_long_5m = time.time()
#         elif timeframe == '15m':
#             last_link_long_15m = time.time()

#         if current_sol == 0:
#             place_tp_long(symbol, amount, tp_price)
#             place_sl_long(symbol, sl_price)
#             print(f"[{symbol} LINK_LONG] 거래량 폭발 롱 진입 (첫 매매, TP 걸림) | amount={amount} | price={current_price} | tp={tp_price} | tp_pct={tp_pct}")
#         else:
#             print(f"[{symbol} LINK_LONG] 거래량 폭발 롱 진입 (추가 매수, TP 없음) | amount={amount} | price={current_price}")

#     # -------------------------------------------------
#     # 거래량 폭발 신호 (숏)
#     # -------------------------------------------------
#     else:
#         vol_signal = analyze_volume_spike_drop(
#             symbol=symbol,
#             timeframe=timeframe,
#             side='short'
#         )

#         print(f"[{symbol} LINK_SHORT] VOLUME_SPIKE={vol_signal}")

#         if not vol_signal or not vol_signal["signal"]:
#             print(f"[{symbol} LINK_SHORT] 거래량 폭발 조건 불만족으로 진입 금지")
#             return

#         tp_pct = tp_pct_2 if (tp_pct_2 is not None and vol_signal["range_volatility"] > 0.018) else tp_pct_1
#         tp_price = vol_signal["prev_close"] * (1 - tp_pct)
#         sl_price = vol_signal["prev_close"] * (1 + 0.035)

#         exchange.create_market_sell_order(symbol, amount)

#         last_link_short_trade_time = time.time()
#         if timeframe == '5m':
#             last_link_short_5m = time.time()
#         elif timeframe == '15m':
#             last_link_short_15m = time.time()

#         place_tp_short(symbol, amount, tp_price)
#         place_sl_short(symbol, sl_price)
#         print(f"[{symbol} LINK_SHORT] 거래량 폭발 숏 진입 | amount={amount} | price={current_price} | tp={tp_price}")            
# #==========5m, 15분봉 3틱룰 급락시 진입 전략========

       # LINK 보유 시 5분봉 추매 전략
        # LINK함수는 다이버 조건은 빼서 유명 무실함. 구동하는데 상관은 없어서 그냥 살려둠
        
        # LINK 보유 시 5분봉 추매 전략
        # LINK함수는 다이버 조건은 빼서 유명 무실함. 구동하는데 상관은 없어서 그냥 살려둠
        
        link_position = get_position_amount('LINK/USDT')

        if link_position > 0:
            # 5 분봉 롱
            trade_rsi_close_strategy_link(
                symbol=SOL_SYMBOL,
                market_id=MARKET_ID_SOL,
                timeframe='5m',
                side='long',
                tp_pct_1=0.01,
                tp_pct_2=0.012,
                min_volatility=0.0015,
                price_diff_pct=0.003,
                rsi_raise_pct=0.01,
                min_range_volatility=0.015
            )
            
            # 15 분봉 롱
            trade_rsi_close_strategy_link(
                symbol=SOL_SYMBOL,
                market_id=MARKET_ID_SOL,
                timeframe='15m',
                side='long',
                tp_pct_1=0.012,
                tp_pct_2=0.015,
                min_volatility=0.0015,
                price_diff_pct=0.003,
                rsi_raise_pct=0.01,
                min_range_volatility=0.015
            )

        elif link_position < 0:
            # 5 분봉 숏
            trade_rsi_close_strategy_link(
                symbol=SOL_SYMBOL,
                market_id=MARKET_ID_SOL,
                timeframe='5m',
                side='short',
                tp_pct_1=0.01,
                tp_pct_2=0.012,
                min_volatility=0.0015,
                price_diff_pct=0.003,
                rsi_drop_pct=0.01,
                min_range_volatility=0.015
            )
            
            # 15 분봉 숏
            trade_rsi_close_strategy_link(
                symbol=SOL_SYMBOL,
                market_id=MARKET_ID_SOL,
                timeframe='15m',
                side='short',
                tp_pct_1=0.012,
                tp_pct_2=0.015,
                min_volatility=0.0015,
                price_diff_pct=0.003,
                rsi_drop_pct=0.01,
                min_range_volatility=0.015
            )

        time.sleep(1)

#14 꼬리봉 전략
# =================================================
# 1. 데이터 함수
# =================================================

def get_candles_with_bb_current(
    symbol,
    timeframe,
    count=100
):
    """
    현재 진행 중인 봉을 포함하여
    OHLCV + 볼린저 밴드를 반환합니다.

    - 현재 진행 중인 봉을 제거하지 않음
    - RSI는 본 전략에서 사용하지 않으므로 계산하지 않음
    - ETH 15m / 1h 꼬리 조건 분석용

    반환 컬럼:
    - ts, open, high, low, close, volume
    - bb_middle, bb_upper, bb_lower
    - ma20
    """

    tf_ms = {
        '1m': 60_000,
        '3m': 180_000,
        '5m': 300_000,
        '15m': 900_000,
        '30m': 1_800_000,
        '1h': 3_600_000,
        '4h': 14_400_000,
        '1d': 86_400_000,
    }

    interval_ms = tf_ms.get(timeframe)

    if interval_ms is None:
        raise ValueError(f"지원하지 않는 타임프레임입니다: {timeframe}")

    # 현재 진행 중인 봉을 포함한 데이터 조회
    ohlcv = exchange.fetch_ohlcv(
        symbol,
        timeframe=timeframe,
        limit=count + 5
    )

    if ohlcv is None or len(ohlcv) < 25:
        raise ValueError(f"{symbol} {timeframe} 데이터가 부족합니다.")

    df = pd.DataFrame(ohlcv, columns=['ts', 'open', 'high', 'low', 'close', 'volume'])

    # 현재 진행 중인 봉을 포함한 최근 count개 봉 사용
    df = df.tail(count).reset_index(drop=True)

    if len(df) < 25:
        raise ValueError(f"{symbol} {timeframe} 데이터가 부족합니다.")

    # -------------------------------------------------
    # 볼린저 밴드 계산
    # -------------------------------------------------
    bb_length = 20
    bb_std_multiplier = 2.0

    df['bb_middle'] = df['close'].rolling(window=bb_length).mean()
    df['bb_std'] = df['close'].rolling(window=bb_length).std(ddof=0)
    df['bb_upper'] = df['bb_middle'] + bb_std_multiplier * df['bb_std']
    df['bb_lower'] = df['bb_middle'] - bb_std_multiplier * df['bb_std']

    # 기존 코드 호환용
    df['ma20'] = df['bb_middle']

    return df.dropna(
        subset=['bb_middle', 'bb_upper', 'bb_lower']
    ).reset_index(drop=True)

# =================================================
# 2. SOL 꼬리 전략 조건 함수
# =================================================

def get_lower_tail_info(candle):
    """
    롱 반등 전략용 아래꼬리 정보를 계산합니다.

    몸통:
    - |종가 - 시가|

    아래꼬리:
    - 종가 - 저가

    꼬리 비율:
    - 아래꼬리 / 몸통

    꼬리 절대 변동성:
    - 아래꼬리 / 종가

    공통 꼬리 조건:
    - 종가 대비 아래꼬리 길이가 0.1% 이상
    """

    # 시가, 종가, 저가 추출
    open_price = float(candle['open'])
    close_price = float(candle['close'])
    low_price = float(candle['low'])

    # 몸통 크기
    body = abs(close_price - open_price)

    # 아래꼬리 크기
    # 롱 반등 전략에서는 종가 - 저가를 아래꼬리로 사용
    lower_tail = close_price - low_price

    # 몸통이 0이면 꼬리 / 몸통 비율 계산 불가
    if body <= 0:
        tail_ratio = 0.0
    else:
        tail_ratio = lower_tail / body

    # 종가 대비 아래꼬리 크기
    if close_price > 0:
        lower_tail_pct = lower_tail / close_price
    else:
        lower_tail_pct = 0.0

    # 꼬리 길이가 종가 대비 0.1% 이상인지 확인
    tail_size_valid = lower_tail_pct >= 0.001

    return {
        "body": body,
        "lower_tail": lower_tail,
        "tail_ratio": tail_ratio,
        "lower_tail_pct": lower_tail_pct,
        "tail_size_valid": tail_size_valid
    }


def get_candle_body_volatility(candle):
    """
    캔들 몸통 변동성을 계산합니다.

    몸통 변동성 = |종가 - 시가| / 시가

    예시:
    - 시가 100
    - 종가 100.5
    - 몸통 변동성 = 0.5 / 100 = 0.005 = 0.5%
    """

    # 시가와 종가 추출
    open_price = float(candle['open'])
    close_price = float(candle['close'])

    # 시가가 0이면 0으로 반환
    if open_price <= 0:
        return 0.0

    # 몸통 변동성 반환
    return abs(close_price - open_price) / open_price


def analyze_sol_tail_rebound_condition(
    df,
    timeframe
):
    """
    SOL 꼬리 반등 조건을 분석합니다.

    주의:
    - 이 함수는 SOL 캔들 DataFrame을 받습니다.
    - ETH는 이 함수에서 전혀 사용하지 않습니다.
    - ETH 롱 보유 여부는 전략 함수에서만 확인합니다.

    현재 진행 중인 봉을 포함한 df 기준 인덱스:

    - df.iloc[-1]: 현재 진행 중인 봉
    - df.iloc[-2]: 직전 확정봉
    - df.iloc[-3]: 직2전 확정봉
    - df.iloc[-4]: 직3전 확정봉

    기준 꼬리 캔들 우선순위:

    1. 직전 확정봉
    2. 직전봉이 조건을 만족하지 못하면 직2전 확정봉

    볼린저 하단 터치 조건은 기준 꼬리 캔들 자체에서 확인:

    - 종가 <= BB 하단 × 1.0006
      → BB 하단보다 최대 +0.06% 위까지 허용

    - 저가 < BB 하단 × 0.999
      → BB 하단보다 최소 0.1% 낮아야 함

    직전 3개 확정봉 range volatility:

    - 대상: 직전봉, 직2전봉, 직3전봉
    - 종가 기준:
      (최고 종가 - 최저 종가) / 최고 종가 >= 1%

    일반 꼬리 조건:

    - 몸통 변동성 > 0.3%
    - 몸통 변동성 < 0.5%
    - 아래꼬리 / 몸통 >= 30%
    - 아래꼬리 / 종가 >= 0.1%

    강한 변동성 꼬리 조건:

    - 몸통 변동성 >= 0.5%
    - 아래꼬리 / 몸통 >= 15%
    - 아래꼬리 / 종가 >= 0.1%
    """

    # 직전봉, 직2전봉, 직3전봉을 보기 위해
    # 최소 4개 이상의 캔들이 필요
    if df is None or len(df) < 4:
        return {
            "signal": False,
            "reason": "SOL 캔들 데이터 부족"
        }

    # -------------------------------------------------
    # 현재봉 및 직전 확정봉 정의
    # -------------------------------------------------
    current = df.iloc[-1]
    prev = df.iloc[-2]
    prev2 = df.iloc[-3]
    prev3 = df.iloc[-4]

    # -------------------------------------------------
    # 기준 꼬리 캔들 후보
    # -------------------------------------------------
    # 직전봉 조건이 충족되면 직전봉을 사용
    # 충족되지 않으면 직2전봉을 사용
    base_candidates = [
        ("prev", prev),
        ("prev2", prev2)
    ]

    # -------------------------------------------------
    # 직전 3개 확정봉 range volatility 계산
    # -------------------------------------------------
    # df.iloc[-4:-1]
    # → 직3전봉, 직2전봉, 직전봉
    last_3_confirmed = df.iloc[-4:-1]

    range_high = float(last_3_confirmed['close'].max())
    range_low = float(last_3_confirmed['close'].min())

    # 최고 종가가 0 이하이면 계산 불가
    if range_high <= 0:
        return {
            "signal": False,
            "reason": "직전 3개 SOL 봉 최고 종가 오류"
        }

    # 직전 3개 봉 종가 기준 range volatility
    range_volatility = (
        range_high - range_low
    ) / range_high

    # 1% 이상이어야 함
    cond_range_volatility = range_volatility >= 0.01

    # -------------------------------------------------
    # 선택된 기준 꼬리 캔들 초기값
    # -------------------------------------------------
    selected_base_candle = None
    selected_base_name = None
    selected_tail_info = None
    selected_body_volatility = None
    selected_condition_type = None
    selected_bb_touch = False

    # -------------------------------------------------
    # 기준 꼬리 캔들 확인
    # -------------------------------------------------
    # 우선순위: 직전봉 → 직2전봉
    for candle_name, candle in base_candidates:

        # 기준 캔들의 가격 정보
        candle_close = float(candle['close'])
        candle_low = float(candle['low'])
        candle_bb_lower = float(candle['bb_lower'])

        # 몸통 변동성, 아래꼬리 정보 계산
        body_volatility = get_candle_body_volatility(candle)
        tail_info = get_lower_tail_info(candle)

        # ---------------------------------------------
        # 볼린저 하단 터치 조건
        # ---------------------------------------------
        # 종가가 BB 하단보다 최대 +0.06% 위까지 허용
        cond_bb_close = (
            candle_close <= candle_bb_lower * 1.0006
        )

        # 저가가 BB 하단보다 0.1% 이상 낮아야 함
        cond_bb_low = (
            candle_low < candle_bb_lower * 0.999
        )

        # 기준 캔들 BB 하단 터치 인정
        cond_bb_touch = (
            cond_bb_close
            and cond_bb_low
        )

        # ---------------------------------------------
        # 일반 꼬리 조건
        # ---------------------------------------------
        # 0.3% < 몸통 변동성 < 0.5%
        # 꼬리 비율 >= 30%
        # 종가 대비 꼬리 >= 0.1%
        cond_normal_tail = (
            body_volatility > 0.003
            and body_volatility < 0.005
            and tail_info["tail_ratio"] >= 0.30
            and tail_info["tail_size_valid"]
        )

        # ---------------------------------------------
        # 강한 변동성 꼬리 조건
        # ---------------------------------------------
        # 몸통 변동성 >= 0.5%
        # 꼬리 비율 >= 15%
        # 종가 대비 꼬리 >= 0.1%
        cond_strong_tail = (
            body_volatility >= 0.005
            and tail_info["tail_ratio"] >= 0.15
            and tail_info["tail_size_valid"]
        )

        # ---------------------------------------------
        # 기준 캔들 최종 선택
        # ---------------------------------------------
        # BB 하단 터치 + 일반 또는 강한 꼬리 조건을
        # 모두 충족하는 첫 캔들을 선택
        if (
            cond_bb_touch
            and (
                cond_normal_tail
                or cond_strong_tail
            )
        ):
            selected_base_candle = candle
            selected_base_name = candle_name
            selected_tail_info = tail_info
            selected_body_volatility = body_volatility
            selected_bb_touch = True

            if cond_normal_tail:
                selected_condition_type = "normal_0.3_to_0.5"
            else:
                selected_condition_type = "strong_over_0.5"

            # 직전봉이 충족되면 바로 선택하고 종료
            # 직전봉 실패 시에만 직2전봉까지 진행
            break

    # 기준 꼬리 캔들이 하나라도 선택되었는지
    cond_base_candle = selected_base_candle is not None

    # -------------------------------------------------
    # 최종 진입 신호
    # -------------------------------------------------
    signal = (
        cond_base_candle
        and cond_range_volatility
    )

    # -------------------------------------------------
    # 신호 미충족 사유
    # -------------------------------------------------
    if signal:
        reason = (
            f"SOL 꼬리 전략 조건 충족 | "
            f"기준={selected_base_name} | "
            f"유형={selected_condition_type} | "
            f"range={range_volatility * 100:.3f}%"
        )
    elif not cond_range_volatility:
        reason = (
            f"직전 3개 SOL 확정봉 range volatility 부족 | "
            f"{range_volatility * 100:.3f}% < 1.000%"
        )
    else:
        reason = (
            "직전/직2전 SOL 기준 캔들의 "
            "꼬리 또는 볼린저 하단 터치 조건 미충족"
        )

    # -------------------------------------------------
    # 분석 결과 반환
    # -------------------------------------------------
    return {
        "signal": signal,
        "reason": reason,

        # 현재 진행 중인 SOL 봉 정보
        "current_open": float(current['open']),
        "current_close": float(current['close']),
        "current_low": float(current['low']),

        # 직전 3개 SOL 확정봉 range volatility 정보
        "range_high_3": float(range_high),
        "range_low_3": float(range_low),
        "range_volatility_3": float(range_volatility),
        "range_volatility_condition": cond_range_volatility,

        # 선택된 기준 SOL 꼬리 캔들 정보
        "base_candle_name": selected_base_name,
        "base_candle_ts": (
            int(selected_base_candle['ts'])
            if selected_base_candle is not None
            else None
        ),
        "base_candle_open": (
            float(selected_base_candle['open'])
            if selected_base_candle is not None
            else None
        ),
        "base_candle_close": (
            float(selected_base_candle['close'])
            if selected_base_candle is not None
            else None
        ),
        "base_candle_low": (
            float(selected_base_candle['low'])
            if selected_base_candle is not None
            else None
        ),
        "base_candle_bb_lower": (
            float(selected_base_candle['bb_lower'])
            if selected_base_candle is not None
            else None
        ),
        "base_body_volatility": (
            float(selected_body_volatility)
            if selected_body_volatility is not None
            else None
        ),
        "base_tail_ratio": (
            float(selected_tail_info['tail_ratio'])
            if selected_tail_info is not None
            else None
        ),
        "base_tail_pct": (
            float(selected_tail_info['lower_tail_pct'])
            if selected_tail_info is not None
            else None
        ),
        "base_bb_touch_condition": selected_bb_touch,
        "base_condition_type": selected_condition_type
    }

# =================================================
# 3. SOL 꼬리 반등 전략 함수
# =================================================

def trade_sol_tail_rebound_strategy(
    eth_symbol,
    sol_symbol,
    market_id,
    timeframe,
    leverage=LEVERAGE,
    stop_loss_pct=0.007,
    min_tp_pct=0.005
):
    """
    ETH 롱 보유 상태에서 SOL 꼬리 반등 조건을 이용해
    SOL 롱에 진입하는 전략.

    ETH의 역할:
    - ETH 롱 포지션 보유 여부만 확인
    - ETH 가격, ETH 캔들, ETH 볼린저 밴드는 사용하지 않음

    SOL의 역할:
    - 꼬리 조건 분석
    - 볼린저 하단 터치 분석
    - 직전 3개 봉 range volatility 분석
    - 실제 SOL 시장가 롱 진입
    - SOL TP 가격 계산
    - SOL 손절 기준 DOGE 헤지 수량 계산

    진입 전제:
    - ETH 롱 포지션 > 0
    - SOL 롱/숏 포지션 = 0
    - SOL 꼬리 조건 충족

    주문 구조:
    - 가용 USDT의 50%를 증거금으로 사용
    - 레버리지 적용
    - SOL 시장가 롱 진입
    - SOL TP 지정가 주문 생성
    - SOL 직접 SL 주문은 생성하지 않음
    - SOL 진입가 대비 -0.7% 기준 DOGE 매수로 손절 헤지
    - DOGE 매수 실패 시 SOL 시장가 긴급 청산
    """

    global last_sol_tail_trade_time
    global last_sol_tail_buy_time_15m
    global last_sol_tail_buy_time_1h

    now = time.time()

    # -------------------------------------------------
    # 전체 공통 쿨다운
    # -------------------------------------------------
    # 꼬리 전략으로 SOL 진입 후 1시간 동안은
    # 15m / 1h 꼬리 전략 모두 신규 진입 금지
    if now - last_sol_tail_trade_time < 3600:
        elapsed = now - last_sol_tail_trade_time

        print(
            f"[{sol_symbol} {timeframe} SOL_TAIL] "
            f"꼬리 전략 전체 공통 쿨다운 중 진입 금지 "
            f"(지난 체결 후 {elapsed:.1f}초 경과)"
        )
        return

    # -------------------------------------------------
    # 15m 전용 쿨다운
    # -------------------------------------------------
    # 15m 4캔들 = 15분 × 4 = 60분
    if (
        timeframe == '15m'
        and now - last_sol_tail_buy_time_15m < 3600
    ):
        minutes_ago = (
            now - last_sol_tail_buy_time_15m
        ) / 60

        print(
            f"[{sol_symbol} {timeframe} SOL_TAIL] "
            f"최근 {minutes_ago:.1f}분 전에 "
            f"15분봉 꼬리 전략 SOL 매수됨 "
            f"(4캔들 / 60분 내 중복매수 금지)"
        )
        return

    # -------------------------------------------------
    # 1h 전용 쿨다운
    # -------------------------------------------------
    # 1h 4캔들 = 1시간 × 4 = 240분 = 4시간
    if (
        timeframe == '1h'
        and now - last_sol_tail_buy_time_1h < 14400
    ):
        minutes_ago = (
            now - last_sol_tail_buy_time_1h
        ) / 60

        print(
            f"[{sol_symbol} {timeframe} SOL_TAIL] "
            f"최근 {minutes_ago:.1f}분 전에 "
            f"1시간봉 꼬리 전략 SOL 매수됨 "
            f"(4캔들 / 240분 내 중복매수 금지)"
        )
        return

    # -------------------------------------------------
    # ETH 롱 보유 여부 확인
    # -------------------------------------------------
    # ETH는 오직 전략 활성화 조건으로만 사용
    # ETH 캔들 / ETH 가격 / ETH 볼린저 밴드는 보지 않음
    eth_position = get_position_amount(eth_symbol)

    if eth_position <= 0:
        print(
            f"[{sol_symbol} {timeframe} SOL_TAIL] "
            f"ETH 롱 미보유로 전략 중단 "
            f"(ETH position={eth_position})"
        )
        return

    # -------------------------------------------------
    # SOL 기존 포지션 확인
    # -------------------------------------------------
    # SOL 롱 또는 SOL 숏 포지션이 하나라도 있으면
    # 신규 진입 금지
    sol_position = get_position_amount(sol_symbol)

    if sol_position != 0:
        print(
            f"[{sol_symbol} {timeframe} SOL_TAIL] "
            f"SOL 기존 포지션 존재로 진입 금지 "
            f"(SOL position={sol_position})"
        )
        return

    # -------------------------------------------------
    # SOL 증거금 모드 및 레버리지 설정
    # -------------------------------------------------
    set_margin_and_leverage(sol_symbol)

    # 가용 USDT 조회
    available_usdt = get_available_usdt()

    # 기존 전략과 동일한 계좌 잔고 범위 제한
    if available_usdt < 2500 or available_usdt > 12000:
        print(
            f"[{sol_symbol} {timeframe} SOL_TAIL] "
            f"계좌 잔고 {available_usdt:.2f} USDT "
            f"범위 밖으로 진입 금지"
        )
        return

    # -------------------------------------------------
    # SOL 현재봉 포함 데이터 조회
    # -------------------------------------------------
    # 현재 진행 중인 봉까지 포함
    # 꼬리 / 볼린저 / range volatility 모두 SOL 기준
    df_sol = get_candles_with_bb_current(
        symbol=sol_symbol,
        timeframe=timeframe,
        count=100
    )

    # -------------------------------------------------
    # SOL 꼬리 전략 조건 분석
    # -------------------------------------------------
    # 아래 함수는 미리 만든 조건 함수입니다.
    #
    # 조건:
    # - 기준봉: 직전봉 우선, 실패 시 직2전봉
    # - BB 하단: 기준봉 close <= bb_lower * 1.0006
    # - BB 이탈: 기준봉 low < bb_lower * 0.999
    # - range volatility:
    #   직전/직2전/직3전 종가 기준 1% 이상
    # - 일반:
    #   몸통 0.3% 초과, 0.5% 미만 + 꼬리비율 30% 이상
    # - 강한:
    #   몸통 0.5% 이상 + 꼬리비율 15% 이상
    tail_signal = analyze_sol_tail_rebound_condition(
        df=df_sol,
        timeframe=timeframe
    )

    print(
        f"[{sol_symbol} {timeframe} SOL_TAIL] "
        f"SOL_TAIL_SIGNAL={tail_signal}"
    )

    # 꼬리 조건 불만족 시 진입 금지
    if not tail_signal or not tail_signal["signal"]:
        print(
            f"[{sol_symbol} {timeframe} SOL_TAIL] "
            f"SOL 꼬리 조건 불만족으로 롱 진입 금지"
        )
        return

    # -------------------------------------------------
    # SOL 현재가 조회
    # -------------------------------------------------
    # 실주문 가격 기준은 SOL 현재가
    sol_entry_price = float(
        exchange.fetch_ticker(sol_symbol)['last']
    )

    if sol_entry_price <= 0:
        print(
            f"[{sol_symbol} {timeframe} SOL_TAIL] "
            f"SOL 현재가 오류: {sol_entry_price}"
        )
        return

    # -------------------------------------------------
    # 주문 수량 계산
    # -------------------------------------------------
    # 가용 USDT의 50%를 증거금으로 사용
    margin_to_use = available_usdt * 0.5

    # 레버리지 적용 후 주문 명목 금액 계산
    notional = margin_to_use * leverage

    # SOL 주문 수량 계산
    # 기존 전략과 맞춰 소수점 셋째 자리까지 반올림
    amount = round(notional / sol_entry_price, 3)

    if amount <= 0:
        print(
            f"[{sol_symbol} {timeframe} SOL_TAIL] "
            f"SOL 주문 수량이 0이라서 중단"
        )
        return

    # -------------------------------------------------
    # SOL TP 가격 계산
    # -------------------------------------------------
    # 조건 함수가 선택한 기준 꼬리 캔들의 시가
    base_candle_open = tail_signal["base_candle_open"]

    # TP = 기준 꼬리 캔들 시가 - 0.05%
    sol_tp_price = base_candle_open * (
        1 - 0.0005
    )

    # 최소 TP = 실제 SOL 진입가 대비 +0.5%
    min_tp_price = sol_entry_price * (
        1 + min_tp_pct
    )

    # 기준 캔들 시가 - 0.05%가
    # 실제 진입가 대비 +0.5%보다 낮으면
    # 최소 +0.5% TP를 사용
    if sol_tp_price < min_tp_price:
        sol_tp_price = min_tp_price

    # -------------------------------------------------
    # SOL 손절 기준 가격
    # -------------------------------------------------
    # 직접 SOL SL 주문은 생성하지 않음
    # DOGE 헤지 수량 계산 기준으로만 기록
    sol_sl_price = sol_entry_price * (
        1 - stop_loss_pct
    )

    # -------------------------------------------------
    # SOL 시장가 롱 진입
    # -------------------------------------------------
    exchange.create_market_buy_order(
        sol_symbol,
        amount
    )

    # -------------------------------------------------
    # 체결 후 꼬리 전략 전용 쿨다운 갱신
    # -------------------------------------------------
    last_sol_tail_trade_time = time.time()

    if timeframe == '15m':
        last_sol_tail_buy_time_15m = time.time()

    elif timeframe == '1h':
        last_sol_tail_buy_time_1h = time.time()

    # -------------------------------------------------
    # SOL TP 주문 생성
    # -------------------------------------------------
    place_tp_long(
        sol_symbol,
        amount,
        sol_tp_price
    )

    # -------------------------------------------------
    # DOGE 수량 기반 손절 헤지
    # -------------------------------------------------
    # SOL 진입가 대비 -0.7% 손절 조건을 기준으로
    # 필요한 DOGE 매수 수량을 계산
    doge_stop_info = calculate_doge_amount_from_sl(
        entry_price=sol_entry_price,
        side='long',
        sl_pct=stop_loss_pct
    )

    doge_amount = doge_stop_info["doge_amount"]
    doge_reference_price = doge_stop_info["sl_reference_price"]

    # -------------------------------------------------
    # DOGE 매수 실행
    # -------------------------------------------------
    # DOGE 매수가 SOL 손절 방어용 역할을 수행
    try:
        buy_doge_for_sol_stop(doge_amount)

    except Exception as e:
        print(
            f"[{sol_symbol} {timeframe} SOL_TAIL] "
            f"DOGE 매수 실패: {e}"
        )

        # DOGE 헤지 매수가 실패했다면
        # SOL 포지션만 남아 손절 방어가 불가능하므로
        # SOL을 즉시 시장가 청산
        try:
            if get_position_amount(sol_symbol) != 0:
                close_position_market(
                    sol_symbol,
                    market_id
                )

                print(
                    f"[{sol_symbol} {timeframe} SOL_TAIL] "
                    f"DOGE 매수 실패 후 SOL 긴급 시장가 청산 완료"
                )

        except Exception as close_error:
            print(
                f"[{sol_symbol} {timeframe} SOL_TAIL] "
                f"DOGE 매수 실패 후 SOL 긴급 청산 실패: "
                f"{close_error}"
            )

        return

    # -------------------------------------------------
    # 최종 진입 로그
    # -------------------------------------------------
    print(
        f"[{sol_symbol} {timeframe} SOL_TAIL] "
        f"SOL 롱 진입 완료 | "
        f"amount={amount} | "
        f"SOL entry={sol_entry_price:.4f} | "
        f"SOL TP={sol_tp_price:.4f} | "
        f"SOL SL 기준={sol_sl_price:.4f} | "
        f"DOGE={doge_amount} | "
        f"DOGE 기준가={doge_reference_price:.6f} | "
        f"SOL 기준캔들={tail_signal['base_candle_name']} | "
        f"SOL range={tail_signal['range_volatility_3'] * 100:.3f}%"
    )

# -------------------------------------------------
# SOL 꼬리 전략 전용 쿨다운 변수
# -------------------------------------------------
last_sol_tail_trade_time = 0
last_sol_tail_buy_time_15m = 0
last_sol_tail_buy_time_1h = 0


        # -------------------------------------------------
        # SOL 꼬리 전략
        # -------------------------------------------------
        # -------------------------------------------------
        # SOL 15분봉 꼬리 조건 → SOL 롱
        # -------------------------------------------------
        # ETH 롱 보유 여부 및 SOL 포지션 유무는
        # 전략 함수 내부에서 확인합니다.
        trade_sol_tail_rebound_strategy(
            eth_symbol='ETH/USDT',
            sol_symbol=SOL_SYMBOL,
            market_id=MARKET_ID_SOL,
            timeframe='15m',
            leverage=LEVERAGE,
            stop_loss_pct=0.007,
            min_tp_pct=0.005
        )

        # -------------------------------------------------
        # SOL 1시간봉 꼬리 조건 → SOL 롱
        # -------------------------------------------------
        # ETH 롱 보유 여부 및 SOL 포지션 유무는
        # 전략 함수 내부에서 확인합니다.
        trade_sol_tail_rebound_strategy(
            eth_symbol='ETH/USDT',
            sol_symbol=SOL_SYMBOL,
            market_id=MARKET_ID_SOL,
            timeframe='1h',
            leverage=LEVERAGE,
            stop_loss_pct=0.007,
            min_tp_pct=0.005
        )

        # 현재 진행 중인 SOL 봉을 감시하므로
        # 3초 간격으로 반복 실행
        time.sleep(3)

        # -------------------------------------------------
        # SOL 꼬리 전략
        # -------------------------------------------------

