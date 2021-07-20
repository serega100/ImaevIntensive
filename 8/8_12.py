import itertools

a = list(itertools.product('СИРОП', repeat=5))
count = 0
for el in a:
    s = ''.join(el)
    if s.count('О') == 1 and s.index('О') != 0 and s[s.index('О')-1] in 'СРП':
        print(s)
        count += 1
print(count)