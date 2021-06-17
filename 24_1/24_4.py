file = open('24_1_3,4,5.txt')
s = file.readline().replace('\n', '')

last = -1
k = 0
max_k = 0

for i in range(len(s)):
    if int(s[i]) >= last:
        k += 1
    else:
        max_k = max(max_k, k)
        k = 1
    last = int(s[i])

print(max_k)