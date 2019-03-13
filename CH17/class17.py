from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd
import csv

style.use('ggplot')
Analysis = 'AAPL.csv'
data = pd.read_csv(Analysis, parse_dates=True, index_col='Date')
price = data['Close']

moving_avg = price.rolling(20).mean()

plt.plot(price, color='b')
plt.plot(moving_avg, color='r')
plt.show()