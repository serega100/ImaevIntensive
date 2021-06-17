for i in range(0,1000):
    s = i
    n = 5
    while s > 23:
        s -= 5
        n *= 2
    if n == 320:
        print(i)