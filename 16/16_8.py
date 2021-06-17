import functools


@functools.lru_cache()
def F(n):
    summ = n-5
    if n > 1:
        summ += n+8
        summ += F(n-2)
        summ += F(n-3)
    return summ


for i in range(1,500):
    print(i, F(i))