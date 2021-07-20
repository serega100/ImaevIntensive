import itertools

a = set(itertools.permutations('ОЛЬГА'))

count = 0
for el in a:
    s = ''.join(el)
    if s[0] != 'Ь' and 'ОЬ' not in s and 'АЬ' not in s:
        print(s)
        count += 1

print(count)