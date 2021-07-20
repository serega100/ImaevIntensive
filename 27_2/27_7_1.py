file = open('27-4a.txt')
n = int(file.readline())
k = 6

minn = 10**10
min_proizv = 10**10
pris = [0] * k

for i in range(k):
    pris[i] = int(file.readline())

for i in range(k,n):
    old = pris[0]
    minn = min(minn, old)

    new = int(file.readline())
    min_proizv = min(min_proizv, minn*new)
    pris = pris[1:] + [new]

print(min_proizv)