# 기존 물량보유시 보류 15분봉 1h봉 쿨다운추가

def analyze_ada_sol_special9(
    symbol='ADA/USDT',
    timeframe='15m'    #15m 되어있어도 실제로는 호출문에서 15m, 1h 결정남
):
    """
    스페셜9: ADA 포지션 연동 SOL 진입 전략.

    - ADA 숏 보유 시 SOL 숏 진입
    - ADA 롱 보유 시 SOL 롱 진입
    - 직전 6~50봉 기준 RSI 및 가격 극값 비교
    - 직1전봉 방향, RSI, 가격, 변동성 조건 적용
    - 직전 2~5봉 극값 조건 적용
    - 직전 2~7봉 시가 기준 range volatility 조건 적용
    - 손절은 직1·직2전 극값 또는 1.3% 중 절대값 작은 값
    - 익절은 직1전 변동성 × 3 또는 1.2% 중 큰 값, 최대 2.5%
    """

    df = get_confirmed_candles_with_rsi(
        symbol,
        timeframe,
        count=100,
        rsi_length=14
    )

    if df is None or len(df) < 60:
        return None

    # =============================================
    # 직1전 확정봉
    # =============================================
    prev_candle = df.iloc[-1]

    prev_open = float(prev_candle["open"])
    prev_high = float(prev_candle["high"])
    prev_low = float(prev_candle["low"])
    prev_close = float(prev_candle["close"])
    prev_rsi = float(prev_candle["rsi"])

    if prev_open <= 0:
        return None

    # =============================================
    # 직1전 몸통 변동성
    # =============================================
    prev_body = abs(
        prev_close - prev_open
    )

    prev_body_volatility = (
        prev_body / prev_open
    )

    cond_prev_volatility = (
        0.002
        <= prev_body_volatility
        <= 0.015
    )

    # =============================================
    # 직전 6~50봉 기준 구간
    # 직1전봉 제외
    # =============================================
    base_50 = df.iloc[-51:-5]

    if len(base_50) < 50:
        return None

    base_lowest_low = float(
        base_50["low"].min()
    )

    base_highest_high = float(
        base_50["high"].max()
    )

    base_lowest_rsi = float(
        base_50["rsi"].min()
    )

    # =============================================
    # 직전 2~5봉 기준 구간
    # 직1전봉 제외
    # =============================================
    recent_4 = df.iloc[-5:-1]

    recent_4_lowest_low = float(
        recent_4["low"].min()
    )

    recent_4_highest_high = float(
        recent_4["high"].max()
    )

    # =============================================
    # 직전 2~7봉 시가 기준 range volatility
    # =============================================
    recent_6 = df.iloc[-7:-1]

    recent_6_opens = recent_6["open"].astype(
        float
    )

    opens_high = float(
        recent_6_opens.max()
    )

    opens_low = float(
        recent_6_opens.min()
    )

    if opens_high <= 0:
        return None

    opens_range_volatility = (
        (opens_high - opens_low)
        / opens_high
    )

    cond_opens_range_volatility = (
        opens_range_volatility < 0.0129  # RV 1.3%미만
    )

    # =============================================
    # ADA 포지션 방향 확인
    # =============================================
    ada_position = get_position_amount(
        "ADA/USDT"
    )

    if ada_position > 0:
        side = "long"
    elif ada_position < 0:
        side = "short"
    else:
        return None

    # =============================================
    # 숏 조건
    # =============================================
    if side == "short":
        cond_prev_direction = (
            prev_close < prev_open
        )

        cond_rsi = (
            prev_rsi
            > base_lowest_rsi - 2
        )

        cond_price = (
            prev_low < base_lowest_low
        )

        cond_recent_price = (
            prev_low
            < recent_4_lowest_low
        )

        cond_base_vs_recent = (
            base_lowest_low
            < recent_4_lowest_low
        )

        sl_reference = max(
            float(df.iloc[-1]["high"]),
            float(df.iloc[-2]["high"])
        )

        fixed_sl_distance = (
            prev_close * 0.013
        )

        sl_distance = min(
            abs(sl_reference - prev_close),
            fixed_sl_distance
        )

        sl_price = (
            prev_close + sl_distance
        )

    # =============================================
    # 롱 조건
    # =============================================
    else:
        cond_prev_direction = (
            prev_close > prev_open
        )

        cond_rsi = (
            prev_rsi
            < base_lowest_rsi + 1
        )

        cond_price = (
            prev_high > base_highest_high
        )

        cond_recent_price = (
            prev_high
            > recent_4_highest_high
        )

        cond_base_vs_recent = (
            base_highest_high
            > recent_4_highest_high
        )

        sl_reference = min(
            float(df.iloc[-1]["low"]),
            float(df.iloc[-2]["low"])
        )

        fixed_sl_distance = (
            prev_close * 0.013
        )

        sl_distance = min(
            abs(prev_close - sl_reference),
            fixed_sl_distance
        )

        sl_price = (
            prev_close - sl_distance
        )

    # =============================================
    # TP 계산
    # =============================================
    tp_distance = max(
        prev_body_volatility * 3,
        0.012
    )

    tp_distance = min(
        tp_distance,
        0.025
    )

    if side == "long":
        tp_price = (
            prev_close * (1 + tp_distance)
        )
    else:
        tp_price = (
            prev_close * (1 - tp_distance)
        )

    # =============================================
    # 전체 조건
    # =============================================
    all_conditions_passed = (
        cond_prev_direction
        and cond_rsi
        and cond_price
        and cond_recent_price
        and cond_base_vs_recent
        and cond_prev_volatility
        and cond_opens_range_volatility
    )

    return {
        "signal": all_conditions_passed,
        "side": side,
        "timeframe": timeframe,
        "prev_open": prev_open,
        "prev_high": prev_high,
        "prev_low": prev_low,
        "prev_close": prev_close,
        "prev_rsi": prev_rsi,
        "prev_body_volatility": (
            prev_body_volatility
        ),
        "base_lowest_low": base_lowest_low,
        "base_highest_high": (
            base_highest_high
        ),
        "base_lowest_rsi": base_lowest_rsi,
        "recent_4_lowest_low": (
            recent_4_lowest_low
        ),
        "recent_4_highest_high": (
            recent_4_highest_high
        ),
        "opens_range_volatility": (
            opens_range_volatility
        ),
        "sl_price": sl_price,
        "tp_price": tp_price,
        "all_conditions_passed": bool(
            all_conditions_passed
        ),
    }
    
    
    
    
def trade_ada_sol_special9(
    symbol='SOL/USDT',
    market_id='SOL/USDT',
    timeframe='15m'
):
    """
    스페셜9: ADA 포지션 연동 SOL 진입 전략.

    - ADA 숏 보유 시 SOL 숏 진입
    - ADA 롱 보유 시 SOL 롱 진입
    - 15m, 1h 타임프레임에서만 동작
    - 15m 쿨다운: 3,600초
    - 1h 쿨다운: 10,800초
    - 같은 방향 SOL 포지션이 있으면 보류
    - 반대 방향 SOL 포지션이 있으면 전량 청산 후 진입
    """

    global last_ada_sol_special9_long_15m
    global last_ada_sol_special9_short_15m
    global last_ada_sol_special9_long_1h
    global last_ada_sol_special9_short_1h

    # =============================================
    # 1. 지원 타임프레임 확인
    # =============================================
    if timeframe not in ("15m", "1h"):
        print(
            f"[{symbol} SPECIAL9] "
            f"지원하지 않는 타임프레임: {timeframe}"
        )
        return

    # =============================================
    # 2. ADA 신호 분석
    # =============================================
    signal = analyze_ada_sol_special9(
        symbol='ADA/USDT',
        timeframe=timeframe
    )

    if signal is None:
        print(
            f"[{symbol} SPECIAL9] "
            "ADA 신호 분석 실패"
        )
        return

    if not signal["signal"]:
        print(
            f"[{symbol} SPECIAL9] "
            "ADA 조건 미충족"
        )
        return

    side = signal["side"]

    # =============================================
    # 3. 쿨다운 확인
    # =============================================
    now = time.time()

    if timeframe == "15m":
        cooldown_seconds = 3600

        if side == "long":
            last_trade_time = (
                last_ada_sol_special9_long_15m
            )
        else:
            last_trade_time = (
                last_ada_sol_special9_short_15m
            )

    else:
        cooldown_seconds = 10800

        if side == "long":
            last_trade_time = (
                last_ada_sol_special9_long_1h
            )
        else:
            last_trade_time = (
                last_ada_sol_special9_short_1h
            )

    if now - last_trade_time < cooldown_seconds:
        remaining = int(
            cooldown_seconds - (
                now - last_trade_time
            )
        )

        print(
            f"[{symbol} SPECIAL9] "
            f"{timeframe} {side.upper()} 쿨다운 중 | "
            f"남은 시간 {remaining}초"
        )
        return

    # =============================================
    # 4. SOL 기존 포지션 확인
    # =============================================
    sol_position = get_position_amount(
        symbol
    )

    # 같은 방향 포지션이 있으면 보류
    if side == "long" and sol_position > 0:
        print(
            f"[{symbol} SPECIAL9] "
            f"기존 SOL 롱 {sol_position}개 보유로 보류"
        )
        return

    if side == "short" and sol_position < 0:
        print(
            f"[{symbol} SPECIAL9] "
            f"기존 SOL 숏 {abs(sol_position)}개 보유로 보류"
        )
        return

    # 반대 방향 포지션이 있으면 전량 청산
    if side == "long" and sol_position < 0:
        print(
            f"[{symbol} SPECIAL9] "
            f"기존 SOL 숏 {abs(sol_position)}개 보유로 전량 청산"
        )

        try:
            close_position_market(
                symbol,
                market_id
            )

        except Exception as e:
            print(
                f"[{symbol} SPECIAL9] "
                f"기존 SOL 숏 청산 실패: {e}"
            )
            return
        # 청산 반영 대기
        time.sleep(0.2)
        
        # 청산 완료 확인
        remaining_position = get_position_amount(
            symbol
        )

        if remaining_position != 0:
            print(
                f"[{symbol} SPECIAL9] "
                f"청산 후에도 SOL 포지션 {remaining_position}개 존재로 진입 중단"
            )
            return        

    elif side == "short" and sol_position > 0:
        print(
            f"[{symbol} SPECIAL9] "
            f"기존 SOL 롱 {sol_position}개 보유로 전량 청산"
        )

        try:
            close_position_market(
                symbol,
                market_id
            )

        except Exception as e:
            print(
                f"[{symbol} SPECIAL9] "
                f"기존 SOL 롱 청산 실패: {e}"
            )
            return
        # 청산 반영 대기
        time.sleep(0.2)
        # 청산 완료 확인
        remaining_position = get_position_amount(
            symbol
        )

        if remaining_position != 0:
            print(
                f"[{symbol} SPECIAL9] "
                f"청산 후에도 SOL 포지션 {remaining_position}개 존재로 진입 중단"
            )
            return

    # =============================================
    # 5. 마진 / 잔고 / 수량 계산
    # =============================================
    set_margin_and_leverage(symbol)

    available_usdt = get_available_usdt()

    if available_usdt <= 0:
        print(
            f"[{symbol} SPECIAL9] "
            "사용 가능 잔고가 없어 진입 금지"
        )
        return

    current_price = float(
        exchange.fetch_ticker(symbol)["last"]
    )

    if current_price <= 0:
        print(
            f"[{symbol} SPECIAL9] "
            f"현재가 오류: {current_price}"
        )
        return

    margin_to_use = available_usdt * 0.5
    notional = margin_to_use * LEVERAGE
    amount = round(
        notional / current_price,
        3
    )

    if amount <= 0:
        print(
            f"[{symbol} SPECIAL9] "
            "주문 수량이 0이라 진입 금지"
        )
        return

    # =============================================
    # 6. SOL 시장가 진입
    # =============================================
    try:
        if side == "long":
            order = exchange.create_market_buy_order(
                symbol,
                amount
            )
        else:
            order = exchange.create_market_sell_order(
                symbol,
                amount
            )

        print(
            f"[{symbol} SPECIAL9] "
            f"ORDER_RESULT={order}"
        )

    except Exception as e:
        print(
            f"[{symbol} SPECIAL9] "
            f"시장가 주문 실패: {e}"
        )
        return

    # =============================================
    # 7. 쿨다운 시간 기록
    # =============================================
    if timeframe == "15m":
        if side == "long":
            last_ada_sol_special9_long_15m = now
        else:
            last_ada_sol_special9_short_15m = now

    else:
        if side == "long":
            last_ada_sol_special9_long_1h = now
        else:
            last_ada_sol_special9_short_1h = now

    # =============================================
    # 8. TP 설정
    # =============================================
    tp_price = signal["tp_price"]

    try:
        if side == "long":
            place_tp_long(
                symbol,
                amount,
                tp_price
            )
        else:
            place_tp_short(
                symbol,
                amount,
                tp_price
            )

        print(
            f"[{symbol} SPECIAL9] "
            f"TP 설정 완료 | tp={tp_price:.6f}"
        )

    except Exception as e:
        print(
            f"[{symbol} SPECIAL9] "
            f"TP 설정 실패: {e}"
        )

        try:
            if get_position_amount(symbol) != 0:
                close_position_market(
                    symbol,
                    market_id
                )
        except Exception as close_error:
            print(
                f"[{symbol} SPECIAL9] "
                f"TP 실패 후 긴급 청산 실패: {close_error}"
            )

        return

    # =============================================
    # 9. DOGE 기반 손절 생성
    # =============================================
    sl_price = signal["sl_price"]

    try:
        if side == "long":
            sl_pct = (
                (current_price - sl_price)
                / current_price
            )
        else:
            sl_pct = (
                (sl_price - current_price)
                / current_price
            )

        if sl_pct <= 0:
            raise ValueError(
                "손절률이 0 이하입니다."
            )

        doge_stop_info = calculate_doge_amount_from_sl(
            entry_price=current_price,
            side=side,
            sl_pct=sl_pct
        )

        doge_amount = doge_stop_info[
            "doge_amount"
        ]

        doge_amount = math.floor(
            doge_amount * 10
        ) / 10

        if doge_amount <= 0:
            raise ValueError(
                "DOGE 손절 수량이 0 이하입니다."
            )

        buy_doge_for_sol_stop(
            doge_amount
        )

        print(
            f"[{symbol} SPECIAL9] "
            f"DOGE 손절 생성 완료 | "
            f"sl_price={sl_price:.6f} | "
            f"sl_pct={sl_pct * 100:.2f}% | "
            f"DOGE={doge_amount}"
        )

    except Exception as e:
        print(
            f"[{symbol} SPECIAL9] "
            f"DOGE 손절 생성 실패: {e}"
        )

        try:
            if get_position_amount(symbol) != 0:
                close_position_market(
                    symbol,
                    market_id
                )
        except Exception as close_error:
            print(
                f"[{symbol} SPECIAL9] "
                f"DOGE 실패 후 긴급 청산 실패: {close_error}"
            )

        return

    print(
        f"[{symbol} SPECIAL9] "
        f"{side.upper()} 진입 완료 | "
        f"timeframe={timeframe} | "
        f"amount={amount} | "
        f"price={current_price:.6f} | "
        f"tp={tp_price:.6f} | "
        f"sl={sl_price:.6f}"
    )   
    
    
    # =============================================
    # 스페셜9: ADA 연동 SOL 진입
    # =============================================
    trade_ada_sol_special9(
        symbol='SOL/USDT',
        market_id='SOL/USDT',
        timeframe='1h'
    )


    trade_ada_sol_special9(
        symbol='SOL/USDT',
        market_id='SOL/USDT',
        timeframe='15m'
    )

