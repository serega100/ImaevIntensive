file = open('27-13b.txt')
n = int(file.readline())
pris = [0] * 7

k1 = 0
k2 = 0
k7 = 0
k14 = 0
count = 0

for i in range(7):
    pris[i] = int(file.readline())

for i in range(7, n):
    old = pris[0]
    new = int(file.readline())

    if old % 14 == 0:
        k14 += 1
    elif old % 7 == 0:
        k7 += 1
    elif old % 2 == 0:
        k2 += 1
    else:
        k1 += 1

    if new % 14 == 0:
        count += k1 + k2 + k7 + k14
    elif new % 7 == 0:
        count += k2 + k14
    elif new % 2 == 0:
        count += k7 + k14
    else:
        count += k14

    pris = pris[1:] + [new]

print(count)