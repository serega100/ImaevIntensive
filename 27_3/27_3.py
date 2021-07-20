file = open('27-3b.txt')
n = int(file.readline())

d_min1 = [10**6, 10**6]
d_min2 = [10**6, 10**6]
min_sum = 0

for line in file.readlines():
    x1, x2 = sorted(map(int, line.split()))
    min_sum += x1
    d = x2 - x1
    if d % 3 == 1:
        if d < d_min1[0] or d < d_min1[1]:
            d_min1 += [d]
            d_min1.remove(max(d_min1))
    elif d % 3 == 2:
        if d < d_min2[0] or d < d_min2[1]:
            d_min2 += [d]
            d_min2.remove(max(d_min2))

if min_sum % 3 == 0:
    print(min_sum)
elif min_sum % 3 == 1:
    print(min(min_sum+min(d_min2), min_sum+d_min1[0]+d_min1[1]))
elif min_sum % 3 == 2:
    print(min(min_sum + min(d_min1), min_sum + d_min2[0] + d_min2[1]))