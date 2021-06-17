import functools


@functools.lru_cache()
def F(n):
    count = 1
    if n >= 1:
        count += 2
        count += F(n-1)
        count += F(n-2)
    return count


print(F(35))