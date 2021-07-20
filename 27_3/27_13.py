file = open('27-30b.txt')
n = int(file.readline())
k = 7
sums = [None] * k

a1, b1, c1 = sorted(map(int, file.readline().split()))
sums[a1%k] = a1
sums[b1%k] = b1
sums[c1%k] = c1

for i in range(n-1):
    c_sums = [None] * k
    a, b, c = map(int, file.readline().split())
    for s in sums:
        if s is not None:
            for x in (a, b, c):
                pair = s + x
                if c_sums[pair%k] is None:
                    c_sums[pair%k] = pair
                else:
                    c_sums[pair%k] = min(pair, c_sums[pair%k])

    sums = c_sums

print(min(sums[1:]))