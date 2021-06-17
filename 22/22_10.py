for i in range(1, 10000):
    x = i
    B = x
    S = -2
    A = 4
    while B // 2 > 0:
        if B % 2 == 0:
            S += A
        else:
            S *= 3
        B //= 2
    if S > 100:
        print(i)
        break