from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [18, 21, 4, 3, 45, 17, 16, 5, 6]

x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y2 = [17, 20, 14, 16, 15, 13, 1, 5, 6]

plt.plot(x, y, linewidth=1)
plt.plot(x2, y2, linewidth=6)

plt.xlabel('X')
plt.ylabel('y')

plt.show()