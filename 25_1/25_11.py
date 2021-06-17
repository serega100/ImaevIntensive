def get_F(n):
    ds = []
    d = 2
    while d * d < n:
        if n % d == 0:
            ds += [d, n//d]
        d += 1
    if d * d == n:
        ds += [d]

    if len(ds) != 0:
        return max(ds) - min(ds)
    else:
        return 0


count = 0
n = 850001
while count != 6:
    F = get_F(n)
    if F != 0 and F % 7 == 0:
        print(n, F, end=' ')
        count += 1
    n += 1