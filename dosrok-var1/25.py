import math


def get_m(n):
    m = 0
    for d in range(2, int(math.sqrt(n))+1):
        if n % d == 0:
            m = (n//d) + d
            break
    return m


count = 0
n = 452022

while count != 5:
    m = get_m(n)
    if m % 7 == 3:
        print(n, m)
        count += 1
    n += 1