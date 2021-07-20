file = open('27-16b.txt')
numbers = map(int, file.readlines()[1:])

k1 = 0
k2 = 0
k13 = 0
k26 = 0
count = 0

for n in numbers:
    if n % 26 == 0:
        count += k1 + k13
        k26 += 1
    elif n % 13 == 0:
        count += k2 + k26
        k13 += 1
    elif n % 2 == 0:
        count += k13
        k2 += 1
    else:
        count += k26
        k1 += 1

print(count)