for n in range(1000, 20000+1):
    ds = [1]
    d = 2
    while d * d < n:
        if n % d == 0:
            ds += [d, n//d]
        d += 1
    if d * d == n:
        ds += [d]

    if n == (sum(ds) + 1):
        print(n, end=' ')