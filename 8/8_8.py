import itertools


def is_glas(symb):
    return symb in 'ОАИ'


a = set(itertools.permutations('ПОЛИНА'))
count = 0
for el in a:
    s = ''.join(el)
    ok = True
    for i in range(1, 6):
        if is_glas(s[i-1]) == is_glas(s[i]):
            ok = False
            break
    if ok:
        print(s)
        count += 1

print(count)