file = open('OKT 27-B.txt')
n = int(file.readline())
k = 3
all_sums = [None] * k

a, b = map(int, file.readline().split())
all_sums[min(a,b)%k] = min(a, b)
all_sums[max(a,b)%k] = max(a, b)

for line in file.readlines():
    x1, x2 = map(int, line.split())
    pairs = []
    for s in all_sums:
        if s is not None:
            pairs += [x1 + s, x2 + s]

    ok_sums = [None] * k
    for s in pairs:
        if ok_sums[s%k] is not None:
            ok_sums[s%k] = min(ok_sums[s%k], s)
        else:
            ok_sums[s%k] = s
    all_sums = ok_sums


print(all_sums)
# [200168565, 200168560, 200168558]