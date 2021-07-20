file = open('27-23b.txt')
n = int(file.readline())
k = 10
sums = [None] * k

a1, b1 = sorted(map(int, file.readline().split()))
sums[a1%k] = a1
sums[b1%k] = b1

for i in range(n-1):
    c_sums = [None] * k
    a, b = map(int, file.readline().split())
    for s in sums:
        if s is not None:
            for x in (a, b):
                pair = s + x
                if c_sums[pair % k] is None:
                    c_sums[pair % k] = pair
                else:
                    c_sums[pair % k] = max(c_sums[pair % k], pair)
    sums = c_sums

sums[5] = -1
print(max(sums))