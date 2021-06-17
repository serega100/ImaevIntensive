import re

file = open('24-s1.txt')

#1
# count = 0
# for line in file.readlines():
#     if re.search('Z.RO', line) is not None:
#         count += 1
# print(count)

#2
count = 0
for line in file.readlines():
    for i in range(len(line)-3):
        if line[i] == 'Z' and line[i+2] == 'R' and line[i+3] == 'O':
            count += 1
            break

print(count)