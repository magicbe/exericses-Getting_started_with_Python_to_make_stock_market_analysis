from pandas_datareader import data as web
from matplotlib import pyplot as plt

# import yahoo_finance as yf
import datetime as dt
import pandas as pd
import csv

# 建立空的csv
# csv_file = '2317.csv'
# out_csv = csv.writer(open(csv_file, 'w'))
Analysis = '2317.csv'

start = dt.datetime(2017, 6, 14)
end = dt.datetime(2018, 6, 14)

df = web.get_data_yahoo(['2317.TW'], start, end)
df.to_csv(Analysis)

# 截取的資料標題有不同，需要轉換
open_txt = csv.reader(open(Analysis, 'r'), delimiter=',')
open_new_txt = []
for row in open_txt:
    if row[0] == 'Attributes':
        tmp_lst = row
    elif row[0] == 'Symbols':
        continue
    elif row[0] == 'Date':
        for i in range(1, len(tmp_lst)):
            row[i] = tmp_lst[i]
        open_new_txt.append(row)
    else:
        open_new_txt.append(row)
out_csv = csv.writer(open(Analysis, 'w', newline='', encoding='UTF-8'))
out_csv.writerows(open_new_txt)

# 顯示收盤價折線圖
data = pd.read_csv(Analysis, parse_dates=True, index_col='Date')
price = data['Close']
# print(price.head())

plt.plot(price)
plt.show()