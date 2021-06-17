def get_m(n):
    d = 2
    while d * d < n:
        if n % d == 0:
            return (n//d) - d
        d += 1
    return 0


count = 0
n = 350001
while count != 6:
    m = get_m(n)
    if m % 23 == 9:
        print(n, m, end=' ')
        count += 1
    n += 1