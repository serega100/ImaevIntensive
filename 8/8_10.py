import itertools
a = list(itertools.product('ИГОРЬ', repeat=8))

count = 0
for el in a:
    s = ''.join(el)
    if s.count('О') == 1 and s.count('Ь') == 1 and s[0] != 'Ь':
        count += 1
print(count)