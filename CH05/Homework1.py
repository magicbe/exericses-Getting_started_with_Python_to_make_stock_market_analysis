# 練習題一：我的錢包
# Sean 每個月的月薪為 3 萬元，每個月 Sean 必須支付勞健保加上稅金共 11%，
# 房租水電為 1 萬 5 千元，吃喝玩樂開銷為 5 千元，其餘薪水定存銀行。
# 請問 Sean 一年可存多少錢？請用 Python 變數和公式算出答案。

salary = 30000
tax_ratio = 0.11
rent = 15000
play = 5000
OneMonthSaving = salary - salary * tax_ratio - rent - play
YearSaving = OneMonthSaving * 12
print("每月定存總金額：", OneMonthSaving)
print("每年定存總金額：", YearSaving)