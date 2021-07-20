file = open('27-11a.txt')
mas = [0] * 8

for line in file.readlines()[1:]:
    vals = map(int, line.split())
    a = [0] * 8
    for s in mas:
        for val in vals:
            new_s = s + val
            a[new_s%8] = max(new_s, a[new_s%8])
    mas = a

print(mas)