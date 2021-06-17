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


max_count = 0
min_num = 999999999
for n in range(2, 20000+1):
    prime_ds = 0
    d = 1
    while d * d < n:
        if n % d == 0:
            if is_prime(d):
                prime_ds += 1
            if is_prime(n//d):
                prime_ds += 1
        d += 1
    if d * d == n and is_prime(d):
        prime_ds += 1
    if prime_ds > max_count:
        max_count = prime_ds
        min_num = n

print(max_count, min_num)