import itertools
a = set(itertools.permutations('АДЖИКА'))

count = 0
for el in a:
    s = ''.join(el)
    ok = True
    for i in range(1, 6):
        if el[i-1] == el[i]:
            ok = False
            break
    if ok:
        count += 1

print(count)