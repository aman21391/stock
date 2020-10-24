import yfinance as yf
import pandas as pd
data = yf.download('AAPL','2006-01-01','2018-10-15')
data.to_csv('appl.csv')