import itertools
a = set(itertools.permutations('КАПКАН'))

count = 0
for el in a:
    s = ''.join(el)
    okay = True
    for i in range(1, 6):
        if s[i-1] == s[i]:
            okay = False
            break
    if okay:
        print(s)
        count +=1

print(count)