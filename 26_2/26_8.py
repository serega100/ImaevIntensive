file = open('26-j6.txt')
# file = open('26-test.txt')
values = sorted(map(int, file.readlines()[1:]), reverse=True)
free_size = sum(values) * 0.9

comp = 0
not_comp = 0
max_not_comp = 0
for i in range(1, len(values)):
    size = sum(values[:i]) * 0.8 + sum(values[i:])
    if size <= free_size:
        comp = i
        not_comp = len(values) - comp
        max_not_comp = max(values[comp:])
        break

for i in range(comp):
    cursor = comp - (i+1)
    size = 0
    maxn = 0
    for j in range(len(values)):
        if j == cursor or j > comp:
            size += values[j]
            maxn = max(maxn, values[j])
        else:
            size += values[j] * 0.8
    if size <= free_size:
        max_not_comp = max(maxn, max_not_comp)

print(not_comp, max_not_comp)
# 6808 71