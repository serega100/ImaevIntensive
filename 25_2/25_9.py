import functools


@functools.lru_cache()
def is_prime(n):
    if n == 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


razn = 0
result = [] # d1, d2
for n in range(326359, 421986+1):
    d = 2
    while d * d < n:
        if n % d == 0 and (n//d) - d > razn and is_prime(d) and is_prime(n//d):
            result = [d, n//d]
            razn = (n//d) - d
        d += 1

print(result)