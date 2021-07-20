file = open('27-4b.txt')
n = int(file.readline())

ostats = [0] * 40
ostats_more_30 = [0] * 40
count = 0

for i in range(n):
    x = int(file.readline())
    if x > 30:
        if x % 40 == 0:
            count += ostats[0]
        else:
            count += ostats[40-x%40]
        ostats[x%40] += 1
        ostats_more_30[x%40] += 1
    else:
        if x % 40 == 0:
            count += ostats_more_30[0]
        else:
            count += ostats_more_30[40-x%40]
        ostats[x%40] += 1

print(count)