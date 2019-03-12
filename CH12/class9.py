def first_function(cost, price, Order):
    ShoesProfit = (price - cost) * Order
    return ShoesProfit

answer = first_function(1500, 2000, Order=300)
print(answer)