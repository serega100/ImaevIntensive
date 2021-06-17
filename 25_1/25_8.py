def product(iterable):
    result = 1
    for el in iterable:
        result *= el
    return result

a = []

for n in range(87921, 88187+1):
    digits = list(map(int, list(str(n))))
    prod = product(digits)
    summ = sum(digits)
    if summ % 14 == 0 and prod != 0 and prod % 18 == 0:
        a += [[prod, summ]]

for el in sorted(a):
    print(el[1], el[0], end=' ')