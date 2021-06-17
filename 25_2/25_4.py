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


for n in range(33333, 55555+1):
    digit_sum = sum(map(int,list(str(n))))
    if is_prime(n) and digit_sum > 35:
        print(n, digit_sum, end=' ')