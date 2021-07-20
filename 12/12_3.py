s = '7' + 55 * '8'

while '78' in s or '7' in s:
    if '788' in s:
        s = s.replace('78', '8887', 1)
    else:
        s = s.replace('7', '8888', 1)
    print(s)
print(s)
print(s.count('8'))