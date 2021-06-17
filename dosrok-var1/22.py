def func(x):
    L = 0
    M = 0
    while x > 0:
        M += 1
        if x % 2 != 0:
            L += 1
        x //= 2
    return (L, M)

n = 0
while func(n) != (5,8):
    n += 1
print(n)