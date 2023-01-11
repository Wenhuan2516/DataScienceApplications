import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

 Shown are the **stock closing price** and ***volume*** of Tesla!
    
""")

# define the ticker symbol
tickerSymbol = 'TSLA'

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this sticker
tickerDf = tickerData.history(period='1d', start='2010-8-31', end='2022-8-31')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)

