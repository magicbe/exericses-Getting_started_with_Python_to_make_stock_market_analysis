from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [18, 21, 4, 3, 45, 17, 16, 5, 6]

x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y2 = [16, 19, 5, 4, 44, 18, 17, 6, 8]

# 折線圖
plt.plot(x, y, linewidth=3, color='b', label='Truth Value')
plt.plot(x2, y2, linewidth=3, marker='o', color='r', linestyle='--', label='Prediction')

plt.xlabel('X')
plt.ylabel('y')

plt.legend()
plt.show()

# 長條圖
plt.bar(x, y, align='center')
plt.bar(x2, y2, align='center')

plt.xlabel('X')
plt.ylabel('y')

plt.show()
