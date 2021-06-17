def get_M(n):
    ds = []
    d = 2
    while d * d < n:
        if n % d == 0:
            ds += [d, n//d]
        d += 1
    if d * d == n:
        ds += [d]

    if len(ds) != 0:
        return min(ds) + max(ds)
    else:
        return 0


count = 0
n = 452022
while count != 5:
    M = get_M(n)
    if M % 7 == 3:
        print(n, M, end=' ')
        count += 1
    n += 1
