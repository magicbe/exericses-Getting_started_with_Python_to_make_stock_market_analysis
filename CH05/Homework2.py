# 練習題二：我的旅行計畫
# Louis 今天要去香港旅遊，旅遊基金有 5 萬新台幣，
# 換成港幣後，預計機票來回為 2000 港幣，飯店為 4000 港幣，
# 吃喝玩樂 5000 港幣，回國後，Louis 換回台幣的錢還剩多少。
# Python 變數和公式算出答案。

TravelFund = 50000
ExchangeRate = 3.7883

Plane = 2000
Hotel = 4000
Play = 5000

HKD = int(TravelFund / ExchangeRate)
print("台幣換港幣為:", HKD, "元")

TotalCost = Plane + Hotel + Play
print("總花費:", TotalCost, "元")

TWD = int((HKD - TotalCost) * ExchangeRate)
print("剩餘台幣:", TWD, "元")