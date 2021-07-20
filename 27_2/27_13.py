file = open('27-4b.txt')
# file = open('27_test.txt')
n = int(file.readline())

max118 = 0
max59 = 0
max2 = 0
max1 = 0
max_result = 0

for i in range(n):
    x = int(file.readline())

    if x % 118 == 0:
        max118 = max(x, max118)
        max_result = max(max_result, max118*max1, max118*max59)
    elif x % 59 == 0:
        max59 = max(x, max59)
        max_result = max(max_result, max59*max2, max59*max118)
    elif x % 2 == 0:
        max2 = max(x, max2)
        max_result = max(max_result, max2*max59)
    else:
        max1 = max(x, max1)
        max_result = max(max_result, max1*max118)

print(max_result)