file = open('24-s1.txt')

count = 0
for line in file.readlines():
    K_count = 0
    U_count = 0
    for symb in line:
        if symb == 'K':
            K_count += 1
        elif symb == 'U':
            U_count += 1
    if K_count > U_count:
        count += 1

print(count)