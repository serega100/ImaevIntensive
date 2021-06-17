file = open('24-j7.txt')
line = file.readline().replace('\n','')

max_k = 0

k = 0
for i in range(1, len(line)):
    if int(line[i-1]) % 2 == int(line[i]) % 2:
        k += 1
    else:
        max_k = max(max_k, k)
        k = 1
print(max_k)