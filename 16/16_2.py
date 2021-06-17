import functools


@functools.lru_cache()
def F(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return F(n//2) + 1
    else:
        return F(n-1) + n


for i in range(1, 1000000000):
    if F(i) == 19:
        print(i)
        break