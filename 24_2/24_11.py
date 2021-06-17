file = open('24-153.txt')
line = file.readline().replace('\n', '')

data = {}

for i in range(2, len(line)):
    if line[i-2] == line[i-1]:
        symb = line[i]
        if symb not in data:
            data[symb] = 1
        else:
            data[symb] += 1

print(data)