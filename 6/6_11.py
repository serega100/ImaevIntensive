for i in range(1, 1000):
    s = i
    n = 5
    while n > 0:
        s = s + n
        n = n - 1
    if s <= 550:
        print(i)