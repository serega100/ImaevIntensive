import re

file = open('24-s1.txt')

#1
count = 0
for line in file.readlines():
    if re.search(r'A.R', line) is not None:
        count += 1

print(count)

#2
# count = 0
# for line in file.readlines():
#     for i in range(len(line)-2):
#         if line[i] == 'A' and line[i+2] == 'R':
#             count += 1
#             break

# print(count)