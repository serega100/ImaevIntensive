def is_prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


for n in range(2532000, 2532160+1):
    if n % 10 == 7 and is_prime(n):
        print(n, end=' ')