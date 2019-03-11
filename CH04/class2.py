ShoesCost = int(input('成本：'))
MarketPrice = int(input('價格：'))
Order = int(input('訂單：'))

ShoesProfit = (MarketPrice - ShoesCost) * Order
print('淨利：', ShoesProfit)