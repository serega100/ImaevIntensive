for i in range(1, 100000):
    x = i
    a = 0
    b = 10
    while x > 0:
        c = x % 10
        a += c
        if c < b:
            b = c
        x = x // 10
    if a == 15 and b == 5:
        print(i)