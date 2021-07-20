file = open('27-31b.txt')
k = 9
sums = [None] * k
n = int(file.readline())

a, b, c = map(int, file.readline().split())
for combo in (a+b, b+c, a+c):
    if sums[combo%k] is None:
        sums[combo % k] = combo
    else:
        sums[combo % k] = min(combo, sums[combo % k])

for i in range(n-1):
    c_sums = [None] * k
    a, b, c = map(int, file.readline().split())
    for s in sums:
        if s is not None:
            for combo in (a+b, b+c, a+c):
                pair = s + combo
                if c_sums[pair%k] is None:
                    c_sums[pair % k] = pair
                else:
                    c_sums[pair % k] = min(c_sums[pair % k], pair)
    sums = c_sums
print(min(sums[1:]))