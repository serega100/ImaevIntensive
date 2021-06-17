import functools

@functools.lru_cache()
def F(n):
    if n < 2:
        return 1
    elif n % 3 == 0:
        return F(n//3) - 1
    else:
        return F(n-1) + 7


count = 0
for i in range(1, 10**6+1):
    if F(i) == 35:
        count += 1

print(count)