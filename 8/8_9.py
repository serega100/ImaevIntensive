import itertools

a = list(itertools.product('АНДРЕЙ', repeat=6))

count = 0
for el in a:
    s = ''.join(el)
    if s.count('Й') <= 1 and s[0] != 'Й' and s[-1] != 'Й' and 'ЙЕ' not in s and 'ЕЙ' not in s:
        print(s)
        count += 1
print(count)