def is_prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


for n in range(4671032, 4671106+1):
    if is_prime(n):
        print(n, end=' ')
