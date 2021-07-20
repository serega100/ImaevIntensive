file = open('27-21b.txt')
n = int(file.readline())
k = 10
sums = [None] * k

a1, b1 = map(int, file.readline().split())
sums[min(a1, b1)%k] = min(a1, b1)
sums[max(a1, b1)%k] = max(a1, b1)

for i in range(n-1):
    a, b = map(int, file.readline().split())
    c_sums = [None] * k
    for s in sums:
        if s is not None:
            for x in (a, b):
                if c_sums[(s+x)%k] is None:
                    c_sums[(s + x) % k] = s+x
                else:
                    c_sums[(s + x) % k] = max(s + x, c_sums[(s + x) % k])
    sums = c_sums

print(sums[8])