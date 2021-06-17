import functools


@functools.lru_cache()
def F(n):
    if n <= 3:
        return n
    elif n % 2 == 0:
        return F(n - 1) + 2 * F(n // 2)
    else:
        return F(n - 1) + F(n - 3)


i = 1
# while F(i) < 10**8:
#     i += 1
# print(i)
print(F(64))
print(F(64) < 10 ** 8)
print(F(65))
print(F(65) < 10 ** 8)
