for n in range(500000, 1000000+1):
    a = [] # Двойной массив [макс.сомнож]
    d = 1
    while d * d <= n:
        if n % d == 0:
            d2 = n // d
            if d2-d <= 90:
                a += [d2]
        d += 1

    if len(a) >= 3:
        print(n, max(a), end=' ')
