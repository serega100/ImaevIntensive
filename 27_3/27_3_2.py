file = open('27-3b.txt')
n = int(file.readline())
mas = [0] * 3

for line in file.readlines():
    x1, x2 = map(int, line.split())
    a = [10**10] * 3
    for s in mas:
        for x in (x1, x2):
            a[(s+x)%3]= min(a[(s+x)%3], s+x)

    mas = a

print(mas)
