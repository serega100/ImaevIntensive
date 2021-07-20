file = open('27-1b.txt')
line_count = int(file.readline())
numbers = list(reversed(sorted(map(int, file.readlines()))))

result1 = set()
result2 = set()
result3 = set()
result6 = set()

pos = 0
while min(len(result1), len(result2), len(result3), len(result6)) < 10:
    n = numbers[pos]
    result1.add(n)
    if n % 6 == 0:
        result2.add(n)
        result3.add(n)
        result6.add(n)
    elif n % 2 == 0:
        result2.add(n)
    elif n % 3 == 0:
        result3.add(n)
    pos += 1

print(list(reversed(list(result1))))
print(list(reversed(list(result6))))
print(list(reversed(list(result2))))
print(list(reversed(list(result3))))

# 999 * 990
# 998 * 999