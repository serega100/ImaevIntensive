for i in range(51, 1000000):
    x = i
    S = 0
    while x > 0:
        if x % 2 > 0:
            S += (x % 7)
        else:
            S -= (x % 7)
        x = x // 7
    if S == 1:
        print(i)
        break