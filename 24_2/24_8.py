a = list(map(str, range(1, 10))) + ['0']
for i in range(26):
    a += [chr(i+65)]

file = open('24-1.txt')
line = file.readline().replace('\n', '')

k = 0
start = ''
max_start = ''
max_len = 0
for i in range(1, len(line)):
    if a.index(line[i-1]) <= a.index(line[i]):
        k += 1
        if start == '':
            start = line[i-1]
    else:
        if max_len < k:
            max_len = k
            max_start = start
            k = 1
            start = ''
print(start, max_len)
print(a.index(start)+1)