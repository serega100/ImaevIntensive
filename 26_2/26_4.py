file = open('26-J5.txt')
before = list(map(int, file.readlines()[1:]))
after = []
on_road = 0

for i in range(len(before)):
    if i == 0 or i == len(before) - 1:
        after += [before[i]]
    else:
        values = [before[i-1], before[i], before[i+1]]
        values.sort()
        after += [values[1]]
        if after[i] < before[i]:
            on_road += before[i] - after[i]

print(after.count(min(after)), on_road)