import itertools
a = list(itertools.product('МЕЧТА', repeat=6))

count = 0
for el in a:
    s = ''.join(el)
    if s.count('А') >= 3:
        count += 1
print(count)