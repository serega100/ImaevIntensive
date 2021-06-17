import functools


@functools.lru_cache()
def F(n):
    summ = n+1
    if n > 1:
        summ += 2*n
        summ += F(n-1)
        summ += F(n-3)
    return summ


for i in range(1,500):
    print(i, F(i))