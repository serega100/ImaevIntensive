file = open('DEK 27-A.txt')

sum1 = 0
sum2 = 0
sum3 = 0
razns = []
chet = 0
nechet = 0

for line in file.readlines()[1:]:
    x1, x2, x3 = sorted(map(int, line.split()))
    if x1 % 2 == 0:
        chet += 1
    else:
        nechet += 1
    if x2 % 2 == 0:
        chet += 1
    else:
        nechet += 1
    sum3 += x1
    razns += [x3-x1, x3-x2]

print(sum3)
print(razns)
print(chet, nechet)