file = open('27-21a.txt')
n = int(file.readline())
razns = []
min_sum = 0

for pair in file.readlines():
    x1, x2 = sorted(map(int, pair.split()))
    razns += [x2-x1]
    min_sum += x1

razns.sort()
print(min_sum)
print(razns)

# 8590
# [19, 34, 47, 55, 57, 76, 85, 107, 127, 215, 219, 242, 295, 295, 347, 444, 445, 495, 723, 799]
# 108