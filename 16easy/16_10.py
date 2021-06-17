def F(n):
    if n == 1:
        return 1
    else:
        return 3 * F(n-1) + G(n-1) - n + 5


def G(n):
    if n == 1:
        return 1
    else:
        return F(n-1) + 3 * G(n-1) - 3 * n

print(F(14) + G(14))