from mpl_finance import candlestick_ohlc
from matplotlib import pyplot as plt
from matplotlib import style

import matplotlib.dates as mdates
import pandas as pd

# 黑背景
style.use('dark_background')
Analysis = 'AAPL.csv'
data = pd.read_csv(Analysis, parse_dates=True, index_col='Date')
price = data['Close']

moving_avg = price.rolling(20).mean()
moving_avg50 = price.rolling(50).mean()
moving_avg80 = price.rolling(80).mean()

moving_avg_mstd = price.rolling(20).std()

# 五五分
# top = plt.subplot(211)
# bottom = plt.subplot(212)

# 九二分
top = plt.subplot2grid((12, 9),(0, 0), rowspan=9, colspan=9)
bottom = plt.subplot2grid((12, 9),(10, 0), rowspan=2, colspan=9)

# 網格
top.grid(which='both', alpha=0.3)

data = data.reset_index()
# 沒有開市的日期不顯示
data['Date'] = data['Date'].apply(lambda d: mdates.date2num(d.to_pydatetime()))
# K線圖
candlestick = [tuple(x) for x in data[['Date', 'Open', 'High', 'Low', 'Close']].values]
candlestick_ohlc(top, candlestick, width=0.5, colorup='r', colordown='g', alpha=0.2)

# top.plot(price, color='b')
top.plot(moving_avg, color='r', linewidth=1, alpha=0.7, label='MA20')
top.plot(moving_avg50, color='b', linewidth=1, alpha=0.7, label='MA50')
top.plot(moving_avg80, color='g', linewidth=1, alpha=0.7, label='MA80')

top.fill_between(moving_avg.index, moving_avg-2*moving_avg_mstd, moving_avg+2*moving_avg_mstd, color='white', alpha=0.1)
bottom.bar(data.index, data['Volume'])

top.legend()
plt.show()