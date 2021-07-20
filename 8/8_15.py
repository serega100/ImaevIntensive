import itertools

a = set(itertools.permutations('КАЛИЙ'))
count = 0
for el in a:
    s = ''.join(el)
    if s[0] != 'Й' and 'ИАК' not in s:
        count += 1

print(count)