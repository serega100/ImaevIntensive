import functools


@functools.lru_cache()
def F(n, m):
    if m == 0:
        return n
    else:
        return F(m, n%m)


count = 0
for n in range(100, 1000+1):
    for d in range(100, 1000 + 1):

