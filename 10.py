import yfinance as yf
import pandas as pd
tickers=['ap','fb','ibm','bp','am']
a=yf.download(tickers,start='2020-08-01',end='2020-08-15')
a.to_csv("data.csv")