import functools


@functools.lru_cache()
def F(n):
    if n <= 5:
        return n
    elif n % 4 == 0:
        return n + F(n//2 - 1)
    else:
        return n + F(n+2)


print(F(16))