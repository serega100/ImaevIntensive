count = 0
for i in range(10000000, 1000000000):
    x = i
    L, M = 0, 0
    while x > 0:
        L += 1
        if x % 16 % 2 == 0:
            M += 1
        else:
            M -= 1
        x //= 16
    if L == 6 and M == 0:
        print(i)
        count += 1
        print('Кол-во:', count)
# 2799744+2115456