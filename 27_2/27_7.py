file = open('27-4b.txt')
count = int(file.readline())

min_proizv = 10**10
minn = 10**10
pris = []

for i in range(6):
    pris += [int(file.readline())]

for i in range(6, count):
    new = int(file.readline())
    old = pris[0]
    minn = min(old, minn)
    min_proizv = min(min_proizv, minn * new)
    pris = pris[1:] + [new]
print(min_proizv)