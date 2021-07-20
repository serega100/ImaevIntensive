import itertools

words = list(itertools.product('ГЕПАРД', repeat=5))
count = 0
for word in words:
    if word.count('Г') == 1 and word[0] != 'А' and word[-1] != 'Е':
        print(word)
        count += 1
print(count)