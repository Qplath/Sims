# Simulated real-time market data generator

import random
from datetime import datetime, timedelta

INITIAL_PRICE = 10000

def init_market_state():
    """Initialize market data in session_state if not present."""
    import streamlit as st
    if "market_price" not in st.session_state:
        st.session_state.market_price = INITIAL_PRICE
    if "market_history" not in st.session_state:
        # 30 data points for line chart
        st.session_state.market_history = [INITIAL_PRICE] * 30
    if "candle_data" not in st.session_state:
        now = datetime.now()
        st.session_state.candle_data = [{
            "time": now - timedelta(minutes=5 * i),
            "open": INITIAL_PRICE,
            "high": INITIAL_PRICE,
            "low": INITIAL_PRICE,
            "close": INITIAL_PRICE
        } for i in reversed(range(30))]

def update_market_data():
    """Update market price, history, and candlestick data in session_state."""
    import streamlit as st
    init_market_state()
    # Simulate new price
    last_price = st.session_state.market_price
    delta = random.randint(-100, 100)
    new_price = max(9000, min(12000, last_price + delta))
    st.session_state.market_price = new_price

    # Update line chart history
    st.session_state.market_history.append(new_price)
    if len(st.session_state.market_history) > 30:
        st.session_state.market_history.pop(0)

    # Update candlestick data
    candle_data = st.session_state.candle_data
    now = datetime.now()
    # Every 5 updates, create a new candle (simulate 5s = 5min)
    if "candle_tick" not in st.session_state:
        st.session_state.candle_tick = 0
    st.session_state.candle_tick += 1
    if st.session_state.candle_tick >= 5:
        # Start new candle
        prev_close = candle_data[-1]["close"]
        new_candle = {
            "time": now,
            "open": prev_close,
            "high": new_price,
            "low": new_price,
            "close": new_price
        }
        candle_data.append(new_candle)
        if len(candle_data) > 30:
            candle_data.pop(0)
        st.session_state.candle_tick = 0
    else:
        # Update last candle
        candle = candle_data[-1]
        candle["close"] = new_price
        candle["high"] = max(candle["high"], new_price)
        candle["low"] = min(candle["low"], new_price)
    st.session_state.candle_data = candle_data

def get_market_data():
    """Return current price, change, and history for dashboard."""
    import streamlit as st
    init_market_state()
    price = st.session_state.market_price
    history = st.session_state.market_history
    if len(history) > 1:
        change = round((price - history[-2]) / history[-2] * 100, 2)
    else:
        change = 0.0
    return {"price": price, "change": change, "history": history}

def get_candlestick_data():
    """Return candlestick data for chart."""
    import streamlit as st
    init_market_state()
    data = st.session_state.candle_data
    return {
        "time": [c["time"] for c in data],
        "open": [c["open"] for c in data],
        "high": [c["high"] for c in data],
        "low": [c["low"] for c in data],
        "close": [c["close"] for c in data]
    }