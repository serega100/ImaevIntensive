for i in range(81, 100000):
    x = i
    s = 0
    while x > 0:
        s += x % 9
        x //= 3
    if s == 17:
        print(i)
        break