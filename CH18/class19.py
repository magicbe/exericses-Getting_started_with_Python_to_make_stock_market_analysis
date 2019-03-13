from mpl_finance import candlestick_ohlc
from matplotlib import pyplot as plt
from matplotlib import style

import matplotlib.dates as mdates
import pandas as pd

style.use('ggplot')
Analysis = 'AAPL.csv'
data = pd.read_csv(Analysis, parse_dates=True, index_col='Date')
price = data['Close']

moving_avg = price.rolling(20).mean()
moving_avg_mstd = price.rolling(20).std()

top = plt.subplot(211)
bottom = plt.subplot(212)

data = data.reset_index()
# 沒有開市的日期不顯示
data['Date'] = data['Date'].apply(lambda d: mdates.date2num(d.to_pydatetime()))
# K線圖
candlestick = [tuple(x) for x in data[['Date', 'Open', 'High', 'Low', 'Close']].values]
candlestick_ohlc(top, candlestick, width=0.5, colorup='r', colordown='g', alpha=0.2)

# top.plot(price, color='b')
top.plot(moving_avg, color='r')
top.fill_between(moving_avg.index, moving_avg-2*moving_avg_mstd, moving_avg+2*moving_avg_mstd, color='b', alpha=0.2)
bottom.bar(data.index, data['Volume'])

plt.show()