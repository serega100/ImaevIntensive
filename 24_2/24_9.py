file = open('k7-m25.txt')
line = file.readline()

count = 0
last_i = 0
for i in range(len(line)-3):
    left = line[i]
    mid = line[i+1]
    right = line[i+2]
    
    if mid > left and mid > right:
        count += 1
        last_i = i

print(count, last_i)