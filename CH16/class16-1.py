import csv
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

Analysis = 'Data.txt'
csv_file = 'Data.csv'

# open_txt = csv.reader(open(Analysis, 'r'), delimiter=',')
# out_csv = csv.writer(open(csv_file, 'w', newline='', encoding='UTF-8'))
# out_csv.writerow(['筆數', '價格'])
# out_csv.writerows(open_txt)

data = pd.read_csv(csv_file, parse_dates=True, index_col='筆數')

print(data)

price = data['價格']

plt.plot(price)
plt.show()