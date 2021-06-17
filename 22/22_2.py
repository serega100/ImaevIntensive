for i in range(1, 10000):
    x = i
    k = x % 7
    a = 0
    b = 0
    while x > 0:
        d = x % 7
        if d == k:
            a += 1
        b += d
        x //= 7
    if a == 4 and b == 11:
        print(i)