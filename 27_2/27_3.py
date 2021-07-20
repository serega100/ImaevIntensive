file = open('27-10b.txt')
numbers = list(map(int, file.readlines()[1:]))
numbers.sort()

k1 = 0
k2 = 0
k5 = 0
k10 = 0
count = 0
for n in numbers:
    if n % 10 == 0:
        count += k1 + k2 + k5 + k10
        k10 += 1
    elif n % 5 == 0:
        count += k2 + k10
        k5 += 1
    elif n % 2 == 0:
        count += k5 + k10
        k2 += 1
    else:
        count += k10
        k1 += 1
print(count)