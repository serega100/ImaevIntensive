count = 0
summ = 0
for n in range(3672, 9117+1):
    if (n % 3 == 2) and (n % 5 == 4):
        count += 1
        summ += n
print(count, summ)