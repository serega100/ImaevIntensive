file = open('24-s1.txt')

count = 0
for line in file.readlines():
    S_count = 0
    X_count = 0
    for symb in line:
        if symb == 'X':
            X_count += 1
        elif symb == 'S':
            S_count += 1

    if S_count == X_count:
        count += 1

print(count)