file = open('26-J1.txt')
a = list(map(int, file.readlines()[1:]))

count = 0
for i in range(1, 50):
    count += min(a.count(i), a.count(100-i))

count += a.count(50)//2
print(count)