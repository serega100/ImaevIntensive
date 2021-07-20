file = open('27-26b.txt')
n = int(file.readline())
k = 16
sums = [None] * k

a1, b1 = map(int, file.readline().split())
sums[min(a1,b1)%k] = min(a1,b1)
sums[max(a1,b1)%k] = max(a1,b1)

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
                    c_sums[pair % k] = min(c_sums[pair % k], pair)
    print(c_sums)
    sums = c_sums
print(sums[15])