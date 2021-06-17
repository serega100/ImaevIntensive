file = open('24.txt')
line = file.readline()

#1
# max_len = 0
# for word in line.split('XZZY'):
#     word_len = len(word) + 6
#     max_len = max(word_len, max_len)
# print(max_len)
# 1713

# 2
k = 3
max_k = 0
for i in range(3, len(line)):
    if line[i-3] == 'X' and line[i-2] == 'Z' and line[i-1] == 'Z' and line[i] == 'Y':
        max_k = max(max_k, k)
        k = 3
    else:
        k += 1
print(max_k)