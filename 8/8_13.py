from itertools import product

a = list(product('ПИРОГ', repeat=6))
count = 0
for el in a:
    s = ''.join(el)
    if s.count('Р') == 1 and s[-1] != 'Р' and s[s.index('Р')+1] in 'ИО':
        count += 1

print(count)