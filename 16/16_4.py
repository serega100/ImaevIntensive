import functools


@functools.lru_cache()
def F(n):
    if n < 3:
        return n + 1
    elif n % 2 == 0:
        return n + 2 * F(n+2)
    else:
        return F(n-2) + n - 2

count = 0
for n in range(1, 100):
    try:
        val = F(n)
        print(n, val)
        if 100 <= val <= 999:
            count += 1
    except RecursionError:
        print(n, None)

print(count)