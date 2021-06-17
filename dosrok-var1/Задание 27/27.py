razns = []

file = open('27_B.txt')
max_sum = 0

for line in file.readlines()[1:]:
    x1, x2, x3 = sorted(map(int, line.split()))
    max_sum += x3
    if (x3-x1) % 109 != 0:
        razns += [x3-x1]
    if (x3-x2) % 109 != 0:
        razns += [x3-x2]

print(max_sum)
razns.sort()
print(razns)

# 8819096478
# [7718]