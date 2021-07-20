file = open('27-11b.txt')
n = int(file.readline())
k = 8
sums = [None] * k

a1, b1, c1 = map(int, file.readline().split())

for x in sorted([a1,b1,c1]):
    sums[x%k] = x

for i in range(n-1):
    a, b, c = map(int, file.readline().split())
    c_sums = [None] * k
    for s in sums:
        if s is not None:
            for x in (a, b, c):
                ost = (s+x) % k
                if c_sums[ost] is None:
                    c_sums[ost] = s + x
                else:
                    c_sums[ost] = max(c_sums[ost], s+x)
    sums = c_sums

print(sums[0])