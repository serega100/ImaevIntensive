file = open('26-k2.txt')
N, K = map(int, file.readline().split(' '))
a = list(map(int, file.readlines()))
a.sort()
a = a[K:-K]
print(a[-1], sum(a)//len(a))