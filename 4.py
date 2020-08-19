import pandas_datareader as web
import datetime
start = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2019, 12, 31)
tickers=['ibm','TSLA', 'FB','MSFT','AAPL']
df = web.data.get_data_yahoo( tickers, start, end)
df.to_csv('data2.csv')