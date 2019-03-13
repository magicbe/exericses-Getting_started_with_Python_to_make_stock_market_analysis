from matplotlib import pyplot as plt
from matplotlib import style
import csv

style.use('ggplot')

x = []
y = []

Analysis = 'Data.txt'

with open(Analysis, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[1])

plt.plot(x, y, label='Price', color='b')
plt.legend()
plt.show()