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


found = []

for n in range(351627, 428763+1):
    d = 2
    while d * d < n:
        if n % d == 0 and is_prime(d) and is_prime(n//d):
            found += [n]
            break
        d += 1

print(len(found), sum(found)//len(found))