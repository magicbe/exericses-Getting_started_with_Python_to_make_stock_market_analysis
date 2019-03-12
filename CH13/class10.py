class first_class:
    def first_function(self, cost, price, order):
        ShoesProfit = (price - cost) * order
        return ShoesProfit

    def second_function(self):
        print('This is my 2nd function in class')

    def third_function(self):
        print('This is my 3rd function in class')

    def fourth_function(self):
        print('This is my 4th function in class')

classCalculation = first_class()
answer = classCalculation.first_function(100, 2000, 3000)
print(answer)