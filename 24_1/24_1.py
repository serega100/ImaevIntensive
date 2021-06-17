file = open('24_1_1,2.txt')
s = file.readline()

a = ['Z', 'Y', 'X']
last = -1
k = 0
max_k = 0

for symb in s:
    if a.index(symb) >= last:
        k += 1
    else:
        max_k = max(k, max_k)
        k = 1
    last = a.index(symb)

print(max_k)