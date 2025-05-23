import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

st.set_page_config(page_title="TSLA Short Interest Tracker", layout="wide")

st.title("Tesla (TSLA) Short Interest Tracker")
st.markdown("Tracks Tesla stock price alongside manually updated short interest estimates.")

# Load manually updated short interest
try:
    short_df = pd.read_csv("short_interest.csv", parse_dates=["Date"])
except FileNotFoundError:
    st.error("short_interest.csv not found. Please upload a CSV file with Date and Short Interest columns.")
    st.stop()

# Get recent TSLA price data
tsla = yf.Ticker("TSLA")
price_data = tsla.history(period="3mo")
price_data.reset_index(inplace=True)

# Ensure both Date columns are in datetime format
price_data['Date'] = pd.to_datetime(price_data['Date'])
short_df['Date'] = pd.to_datetime(short_df['Date'])

# Merge price and short interest
merged = pd.merge(price_data, short_df, how='left', on='Date')
merged['Short Interest'].fillna(method='ffill', inplace=True)

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