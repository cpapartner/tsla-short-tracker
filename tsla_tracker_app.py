import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

st.set_page_config(page_title="TSLA Short Interest Tracker", layout="wide")

st.title("Tesla (TSLA) Short Interest Tracker")
st.markdown("Tracks Tesla stock price alongside manually updated short interest estimates.")

# Load manually updated short interest
try:
    short_df = pd.read_csv("short_interest.csv")
    short_df['Date'] = pd.to_datetime(short_df['Date'], errors='coerce').dt.date
    short_df.dropna(subset=['Date'], inplace=True)
except Exception as e:
    st.error(f"Error loading short_interest.csv: {e}")
    st.stop()

# Get recent TSLA price data
try:
    tsla = yf.Ticker("TSLA")
    price_data = tsla.history(period="3mo")
    price_data.reset_index(inplace=True)
    price_data['Date'] = pd.to_datetime(price_data['Date'], errors='coerce').dt.date
    price_data.dropna(subset=['Date'], inplace=True)
except Exception as e:
    st.error(f"Error loading TSLA price data: {e}")
    st.stop()

# Merge price and short interest
try:
    merged = pd.merge(price_data, short_df, how='left', on='Date')
    merged['Short Interest'].fillna(method='ffill', inplace=True)
except Exception as e:
    st.error(f"Error during merge: {e}")
    st.stop()

# Plot
fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.set_xlabel("Date")
ax1.set_ylabel("TSLA Price", color='blue')
ax1.plot(merged['Date'], merged['Close'], color='blue', label='TSLA Close')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.set_ylabel("Short Interest (M)", color='red')
ax2.plot(merged['Date'], merged['Short Interest'] / 1_000_000, color='red', label='Short Interest')
ax2.tick_params(axis='y', labelcolor='red')

fig.tight_layout()
st.pyplot(fig)

st.subheader("Latest Data")
st.dataframe(merged.tail(10))