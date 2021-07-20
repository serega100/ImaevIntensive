import itertools
a = list(itertools.product('0123456789', repeat=8))

count = 0
for el in a:
    if int(el) % 5 == 0:
        ok = True
        for i in range(1, 8):
            if int(el[i-1]) % 2 == int(el[i]) % 2:
                ok = False
        if ok:
            count += 1
print(count)