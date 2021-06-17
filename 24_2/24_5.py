import re

file = open('24_2_5.txt')
line = file.readline()

#1
max_len = 0
for word in line.split(' '):
    if word == '':
        continue
    else:
        max_len = max(max_len, len(word))

print(max_len)

max_len = 0
#2
for word in re.findall(r'\S+', line):
    max_len = max(max_len, len(word))

print(max_len)