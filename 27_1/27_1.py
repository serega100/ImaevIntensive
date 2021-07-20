file = open('27v10_B.txt')
n = int(file.readline())
k = 49
summ = [0] * k
a, b = map(int, file.readline().split())
summ[min(a, b) % k] = min(a, b)
summ[max(a, b) % k] = max(a, b)

for line in file.readlines():
    sumt = [0] * k
    a, b = map(int, line.split())
    for i in range(len(summ)):
        if summ[i] != 0:
            sumt[(summ[i] + a) % k] = max(summ[i] + a, sumt[(summ[i] + a) % k])
            sumt[(summ[i] + b) % k] = max(summ[i] + b, sumt[(summ[i] + b) % k])
    summ = sumt
print(max(summ[1:]))