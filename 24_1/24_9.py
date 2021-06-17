file = open('24-1.txt')
s = file.readline()

n = ''
min_n = None
for symb in s:
    if symb in map(str, range(10)):
        n += symb
    elif n != '':
        num = int(n)
        if num % 2 != 0 and (min_n is None or min_n > num):
            min_n = num
        n = ''
print(min_n)