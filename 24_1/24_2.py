file = open('24_1_1,2.txt')
# file = open('24_test.txt')
s = file.readline()

max_k = 0
z_count = 0

for i in range(len(s)):
    k = 1
    left = 1
    right = 1
    if s[i] == 'Z':
        while i-left >= 0 and s[i-left] != 'Z':
            k += 1
            left += 1
        while i+right < len(s) and s[i+right] != 'Z':
            k += 1
            right += 1
        max_k = max(max_k, k)

print(max_k)