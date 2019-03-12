count = [7,7,571,571,517,571,57,7,57,57,57,57]

# for out in count:
#     print(out)

for out in range(20):
    print(out, end=' ')
print()

for out in range(5, 21):
    print(out, end=' ')
print()

for out in range(3, 8, 2):
    print(out, end=' ')
print()

pen = 4

while pen < 10:
    print(pen, end=' ')
    pen += 1
else:
    print('到 else 來', pen)