file = open('26-50.txt')
values = list(map(int, file.readlines()[1:]))
values.sort()

part_4_count = len(values)//4
part_5_count = len(values)//5

count = 0
min_val = None

for x1 in range(len(values)-1):
    for x2 in range(x1+1, len(values)):
        part_4_indexes = list(range(part_4_count))  # Берем четверть сверху + 2 значения ниже
        part_5_indexes = list(range(len(values)))[-part_5_count:]  # Берем пятью часть снизу + 2 значения выше

        # if x1 in part_4_indexes:
        #     part_4_indexes.remove(x1)
        # else:
        #     part_4_indexes = part_4_indexes[:-1]
        #
        # if x1 in part_5_indexes:
        #     part_5_indexes.remove(x1)
        # else:
        #     part_5_indexes = part_5_indexes[1:]
        #
        # if x2 in part_4_indexes:
        #     part_4_indexes.remove(x2)
        # else:
        #     part_4_indexes = part_4_indexes[:-1]
        #
        # if x2 in part_5_indexes:
        #     part_5_indexes.remove(x2)
        # else:
        #     part_5_indexes = part_5_indexes[1:]

        sum_4 = 0
        sum_5 = 0

        for i in part_4_indexes:
            sum_4 += values[i]

        for i in part_5_indexes:
            sum_5 += values[i]

        val_1 = values[x1]
        val_2 = values[x2]
        avg_vals = (val_1+val_2)/2

        if sum_4 < avg_vals < sum_5:
            count += 1
            if min_val is None or avg_vals < min_val:
                min_val = avg_vals

print(count, min_val)