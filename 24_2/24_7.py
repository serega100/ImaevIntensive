file = open('24_2_7.txt')
line = file.readline()

max_len = 0
before = line[0]
k = 0
for i in range(1, len(line)-1):
    k += 1
    if line[i] != line[i+1]:
        after = line[i+1]
        if before == after:
            max_len = max(max_len, k)
        before = line[i]
        k = 0

print(max_len)