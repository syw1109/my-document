
# 5캔들안에 다이버 있었는지 확인하고 1% 하락된 가격으로 진입하는 조건? 요건 ticker xrp 말고 다른거로 하면 되겠다.
# 추매 후 추매 물량은 tp기준으로 털고 싶은데, 그렇게 하자니 폭락시에 다 뚜드려 맞을까봐 무섭네
# 7%하락하는 경우가 많이 없으니, 그럴땐 그냥 2600달러 뚜두려 맞고 끝내고 다음 abc 노리면 되지 않을까


def analyze_bullish_divergence_close_last5(symbol, timeframe, rsi_raise_pct=0.003, min_volatility=0.003, price_diff_pct=0.001):
    """
    직전 5개 확정봉 중에서 bullish divergence 신호가 있었는지 확인.
    가장 최근에 발견된 신호를 반환.
    """
    df = get_confirmed_candles_with_rsi(symbol, timeframe)

    if len(df) < 20:
        return None

    latest_prev_candle = df.iloc[-1]
    latest_prev_close = float(latest_prev_candle["close"])

    found = None

    for i in range(-5, 0):
        candle_idx = len(df) + i
        if candle_idx < 15:
            continue

        candle = df.iloc[candle_idx]
        base_15 = df.iloc[candle_idx - 15:candle_idx]

        if len(base_15) < 15:
            continue

        lowest_close = base_15["close"].min()
        lowest_rsi = base_15["rsi"].min()
        range_high = base_15["close"].max()
        range_low = base_15["close"].min()
        range_volatility = (range_high - range_low) / range_high

        cond_price = candle["close"] < lowest_close * (1 - price_diff_pct)
        cond_rsi = candle["rsi"] >= lowest_rsi * (1 + rsi_raise_pct)
        cond_volatility = abs(candle["close"] - candle["open"]) / candle["open"] >= min_volatility

        if cond_price and cond_rsi and cond_volatility:
            found = {
                "signal": True,
                "lowest_close": float(lowest_close),
                "lowest_rsi": float(lowest_rsi),
                "prev_open": float(candle["open"]),
                "prev_close": float(candle["close"]),
                "prev_rsi": float(candle["rsi"]),
                "range_volatility": float(range_volatility),
                "signal_close": float(candle["close"]),
                "latest_prev_close": latest_prev_close,
                "latest_drop_from_signal_close": (float(candle["close"]) - latest_prev_close) / float(candle["close"])
            }

    if found is None:
        return None

    return found


def trade_rsi_close_strategy_xrp_long(
    symbol,
    market_id,
    timeframe,
    tp_long_pct,
    tp_long_pct_2=None,
    min_volatility=0.003,
    price_diff_pct=0.001,
    rsi_raise_pct=0.003,
    min_range_volatility=0.015
):
    """
    XRP 보유 시 롱 조건만 적용.
    TP 분기 유지:
      - range_volatility > 0.018 이면 tp_long_pct_2
      - 아니면 tp_long_pct
    진입 제약:
      - range_volatility >= 0.015 일 때만 진입
    """
    global last_xrp_long_trade_time, last_xrp_long_1h, last_xrp_long_15m

    if time.time() - last_xrp_long_trade_time < 60:
        print(f"[{symbol} XRP_LONG] 60 초 쿨다운 중 진입 금지 (지난 체결 후 {time.time() - last_xrp_long_trade_time:.1f}초 경과)")
        return

    if timeframe == '1h' and time.time() - last_xrp_long_1h < 7200:
        minutes_ago = (time.time() - last_xrp_long_1h) / 60
        print(f"[{symbol} XRP_LONG 1h] 최근 {minutes_ago:.1f}분 전에 1 시간봉 매수됨 (120 분 내 중복매수 금지)")
        return

    if timeframe == '15m' and time.time() - last_xrp_long_15m < 1800:
        minutes_ago = (time.time() - last_xrp_long_15m) / 60
        print(f"[{symbol} XRP_LONG 15m] 최근 {minutes_ago:.1f}분 전에 15 분봉 매수됨 (30 분 내 중복매수 금지)")
        return

    set_margin_and_leverage(symbol)
    current_balance = get_available_usdt()

    if current_balance < 5500 or current_balance > 12000:
        print(f"[{symbol} XRP_LONG] 계좌 잔고 {current_balance:.2f} USD (6000~12000 밖이므로 진입 금지)")
        return

    xrp_position = get_position_amount('XRP/USDT')
    if xrp_position <= 0:
        print(f"[{symbol} XRP_LONG] XRP 포지션 없음 (롱 진입 금지)")
        return

    n_xrp = abs(xrp_position)
    sol_threshold = 40 * n_xrp
    sol_position = get_position_amount('SOL/USDT')
    current_sol = sol_position if sol_position > 0 else 0

    print(f"[{symbol} XRP_LONG] XRP 보유량: {n_xrp}개, SOL 보유량: {current_sol}개, 기준치: {sol_threshold}개")

    if current_sol > sol_threshold:
        print(f"[{symbol} XRP_LONG] SOL 보유량 {current_sol}개 > 기준 {sol_threshold}개로 매수 금지")
        return

    current_price = float(exchange.fetch_ticker(symbol)['last'])
    available_usdt = get_available_usdt()
    margin_to_use = available_usdt * 0.5
    notional = margin_to_use * LEVERAGE
    amount = round(notional / current_price, 3)

    if amount <= 0:
        print(f"[{symbol} XRP_LONG] 주문 수량이 0 이라서 중단")
        return

    if current_sol == 0:
        bull_close = analyze_bullish_divergence_close(
            symbol=symbol,
            timeframe=timeframe,
            rsi_raise_pct=rsi_raise_pct,
            min_volatility=min_volatility,
            price_diff_pct=price_diff_pct
        )

        print(f"[{symbol} XRP_LONG] BULL_CLOSE={bull_close}")

        if not bull_close or not bull_close["signal"]:
            print(f"[{symbol} XRP_LONG] CLOSE 기준 진입 조건 없음")
            return

        if bull_close["range_volatility"] < min_range_volatility:
            print(f"[{symbol} XRP_LONG] range_volatility {bull_close['range_volatility']*100:.2f}% 미만으로 진입 금지")
            return

        try:
            cme_price = get_last_saturday_6_close()
        except Exception as e:
            print(f"[{symbol} XRP_LONG] 토요일 06:00 가격 조회 실패: {e}")
            return

        deviation = abs(bull_close["prev_close"] - cme_price) / cme_price
        if deviation < 0.01:
            print(f"[{symbol} XRP_LONG] CME 편차 {deviation*100:.2f}% 미만으로 진입 금지 | CME={cme_price:.2f}, prev_close={bull_close['prev_close']:.2f}")
            return

        print(f"[{symbol} XRP_LONG] CME 편차 {deviation*100:.2f}% 충족 | CME={cme_price:.2f}, prev_close={bull_close['prev_close']:.2f}")

        tp_pct = tp_long_pct_2 if (tp_long_pct_2 is not None and bull_close["range_volatility"] > 0.018) else tp_long_pct
        tp_price = bull_close["prev_close"] * (1 + tp_pct)
        sl_price = bull_close["prev_close"] * (1 - 0.07)

        exchange.create_market_buy_order(symbol, amount)

        last_xrp_long_trade_time = time.time()
        if timeframe == '1h':
            last_xrp_long_1h = time.time()
        elif timeframe == '15m':
            last_xrp_long_15m = time.time()

        place_tp_long(symbol, amount, tp_price)
        place_sl_long(symbol, amount, sl_price)
        print(f"[{symbol} XRP_LONG] CLOSE 기준 롱 진입 (첫 매매, TP/SL 걸림) | amount={amount} | price={current_price} | tp={tp_price} | sl={sl_price} | tp_pct={tp_pct}")
        return

    bull_close_5 = analyze_bullish_divergence_close_last5(
        symbol=symbol,
        timeframe=timeframe,
        rsi_raise_pct=rsi_raise_pct,
        min_volatility=min_volatility,
        price_diff_pct=price_diff_pct
    )

    print(f"[{symbol} XRP_LONG] BULL_CLOSE_LAST5={bull_close_5}")

    if not bull_close_5 or not bull_close_5["signal"]:
        print(f"[{symbol} XRP_LONG] 최근 5개봉 기준 진입 조건 없음")
        return

    if bull_close_5["range_volatility"] < min_range_volatility:
        print(f"[{symbol} XRP_LONG] range_volatility {bull_close_5['range_volatility']*100:.2f}% 미만으로 진입 금지")
        return

    if bull_close_5["latest_drop_from_signal_close"] < 0.01:
        print(f"[{symbol} XRP_LONG] 신호봉 종가 대비 최근 직전봉 종가가 1% 이상 낮지 않아 추가 진입 금지")
        return

    try:
        cme_price = get_last_saturday_6_close()
    except Exception as e:
        print(f"[{symbol} XRP_LONG] 토요일 06:00 가격 조회 실패: {e}")
        return

    deviation = abs(bull_close_5["latest_prev_close"] - cme_price) / cme_price
    if deviation < 0.01:
        print(f"[{symbol} XRP_LONG] CME 편차 {deviation*100:.2f}% 미만으로 진입 금지 | CME={cme_price:.2f}, prev_close={bull_close_5['latest_prev_close']:.2f}")
        return

    print(f"[{symbol} XRP_LONG] CME 편차 {deviation*100:.2f}% 충족 | CME={cme_price:.2f}, prev_close={bull_close_5['latest_prev_close']:.2f}")

    tp_pct = tp_long_pct_2 if (tp_long_pct_2 is not None and bull_close_5["range_volatility"] > 0.018) else tp_long_pct
    tp_price = bull_close_5["latest_prev_close"] * (1 + tp_pct)
    sl_price = bull_close_5["latest_prev_close"] * (1 - 0.07)

    exchange.create_market_buy_order(symbol, amount)

    last_xrp_long_trade_time = time.time()
    if timeframe == '1h':
        last_xrp_long_1h = time.time()
    elif timeframe == '15m':
        last_xrp_long_15m = time.time()

    print(f"[{symbol} XRP_LONG] CLOSE 기준 롱 진입 (추가 매수, TP 없음) | amount={amount} | price={current_price}")