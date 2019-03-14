from pandas_datareader import data as web
from matplotlib import pyplot as plt

import yahoo_finance as yf
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
