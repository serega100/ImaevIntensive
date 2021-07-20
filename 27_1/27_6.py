file = open('MART 27-B.txt')
n = int(file.readline())
numbers = [[], [], []]
for line in file.readlines():
    x = int(line)
    numbers[x % 3] += [x]

for sub in numbers:
    sub.sort()
# 0 0 0
# 0 1 2
# 1 1 1
case1 = sum(numbers[0][:3])
case2 = numbers[0][0] + numbers[1][0] + numbers[2][0]
case3 = sum(numbers[1][:3])
print(case1, case2, case3)
print(min(case1, case2, case3))