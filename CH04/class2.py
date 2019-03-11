# Python 小邏輯
# 某某工廠生產一雙鞋子的成本為 100 元，
# 在市面上賣 200 元，今天接收到了 3000 筆的訂單，
# 請用 Python 算出淨利。

ShoesCost = int(input('成本：'))
MarketPrice = int(input('價格：'))
Order = int(input('訂單：'))

ShoesProfit = (MarketPrice - ShoesCost) * Order
print('淨利：', ShoesProfit)