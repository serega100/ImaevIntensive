for i in range(1, 100000000000000000):
    x = i
    a = 0
    b = 0
    while x > 0:
        if x % 2 == 0:
            a += 1
        else:
            b += 1
        x //= 2
    if a == 10 and b == 8:
        print(i)