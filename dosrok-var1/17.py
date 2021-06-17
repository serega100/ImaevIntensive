count = 0
minn = 0

for n in range(16015, 48989+1):
    if ((n % 7 == 0) or (n % 11 == 0)) and (n % 9 != 0) and (n % 12 != 0) and (n % 13 != 0):
        count += 1
        if minn == 0:
            minn = n

print(count, minn)