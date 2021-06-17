file = open('k7a-5.txt')
s = file.readline()

k = 0
max_k = 0

for symb in s:
    if symb not in ['C', 'F']:
        k += 1
    else:
        max_k = max(max_k, k)
        k = 0

print(max_k)