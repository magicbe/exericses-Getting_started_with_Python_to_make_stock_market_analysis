'''
class 5 list leaning
'''

shop = ['milk', 'orange' ,'beef', 'apple', 'water', 'tea', 'hot dog', 'drink']
print(shop)
print(shop[1])
print(shop[-1])

shop[0] = 'soda'
print(shop)

count = [4, 5, 6, 7, 8, 9, 10]
print(count)
print(sum(count))

print(max(count))
print(min(count))
print(sorted(count))

total = shop + ['cheese']
print(total)

del shop[0]
print(shop)

shop.append('banana')
print(shop)

shop.clear()
print(shop)