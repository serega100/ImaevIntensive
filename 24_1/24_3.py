file = open('24_1_3,4,5.txt')
s = file.readline()

k = 0
max_k = 0

for i in range(len(s)-1):
    k += 1
    if s[i] == s[i+1]:
        max_k = max(max_k, k)
        k = 0

print(max_k)