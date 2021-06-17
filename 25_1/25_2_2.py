for n in range(81234, 134689+1):
    d = 2
    ds = []

    while d * d < n:
        if n % d == 0:
            ds += [d, n//d]
        d += 1

    if d*d == n and len(ds) == 2:
        print(ds)

# 17 4913 19 6859