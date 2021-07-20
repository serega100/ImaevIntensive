file = open('26-j2.txt')
values = sorted(map(int, file.readlines()[1:]))
medium = values[len(values)//2]
avg = sum(values)/len(values)

count = 0
for val in values:
    if min(medium, avg) <= val <= max(medium, avg):
        count += 1
print(count)