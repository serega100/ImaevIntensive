file = open('27-15b.txt')
n = int(file.readline())
pris = [0] * 5
ostats = [0] * 14
count = 0

for i in range(5):
    pris[i] = int(file.readline())

for i in range(5, n):
    old = pris[0]
    print(old, old % 14)
    ostats[old % 14] += 1

    new = int(file.readline())
    ost = new % 14
    if ost == 0:
        count += ostats[0]
    else:
        count += ostats[14-ost]

    pris = pris[1:] + [new]

print(ostats)
print(count)