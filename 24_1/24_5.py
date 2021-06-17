file = open('24_1_3,4,5.txt')
s = file.readline().replace('\n', '')

k = 0
max_k = 0
for i in range(len(s)):
    if int(s[i]) % 2 != 0:
        k += 1
    else:
        max_k = max(max_k, k)
        k = 0

print(max_k)