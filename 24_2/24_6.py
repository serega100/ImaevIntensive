file = open('24_2_6.txt')
line = file.readline()

d_count = 0
e_count = 0
for i in range(len(line)-4):
    a = line[i]
    b = line[i+1]
    c = line[i+2]
    d = line[i+3]
    if a not in [b, c, d] and b not in [c, d] and c != d:
        if 'd' in line[i:i+4]:
            d_count += 1
        if 'e' in line[i:i+4]:
            e_count += 1
print(abs(d_count-e_count))
