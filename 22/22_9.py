count = 0
for i in range(1, 501):
    x = i
    S = 0
    while x > 0:
        if x % 5 > 0:
            S += (x % 5)
        else:
            S *= (x % 5)
        x = x // 5
    if S == 13:
        count += 1


print(count)