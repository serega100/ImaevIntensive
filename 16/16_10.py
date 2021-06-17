import functools


@functools.lru_cache()
def F(n):
    print(n)
    if n > 0:
        d = (n%10 + F(n//10))
        print(d)
        return d
    else:
        return 0


@functools.lru_cache()
def F2(n, time=1):
    if time == 2:
        return n
    if n > 0:
        return F2(n // 10, time + 1)


for i in range(1, 10000):
    if F2(i) > 51:
        print(i, F(i))
        break