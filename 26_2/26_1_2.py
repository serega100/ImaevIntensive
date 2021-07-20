file = open('26-50.txt')
values = list(map(int, file.readlines()[1:]))
values.sort()

part_4_min = values[len(values)//4]
part_5_min = values[4*len(values)//5]
count = 0
min_avg = 10 ** 8

for x1 in range(len(values)-1):
    for x2 in range(x1+1, len(values)):
        if (x1 + x2) % 2 != 0:
            continue

        avg = (x1+x2)//2
        if part_4_min < avg < part_5_min:
            count += 1
            min_avg = min(avg, min_avg)
            print((x1, x2))

print(count, min_avg)