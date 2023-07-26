import pandas as pd
import yfinance as yf

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data on the ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for the ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2023-1-1')

# Calculate the 50-day moving average
tickerDf['MA50'] = tickerDf['Close'].rolling(window=50).mean()

# Print the most recent data
print(tickerDf.tail())
