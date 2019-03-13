from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd
import csv

style.use('ggplot')
Analysis = 'AAPL.csv'
data = pd.read_csv(Analysis, parse_dates=True, index_col='Date')
price = data['Close']

moving_avg = price.rolling(20).mean()
moving_avg_mstd = price.rolling(20).std()

top = plt.subplot(211)
bottom = plt.subplot(212)

top.plot(price, color='b')
top.plot(moving_avg, color='r')
top.fill_between(moving_avg.index, moving_avg-2*moving_avg_mstd, moving_avg+2*moving_avg_mstd, color='b', alpha=0.2)
bottom.bar(data.index, data['Volume'])

plt.show()