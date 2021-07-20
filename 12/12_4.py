s = '1'*13 + '2'*13 + '3'*13

while '11' in s:
    s = s.replace('11', '2', 1)
    print(s)
    s = s.replace('22', '3', 1)
    print(s)
    s = s.replace('33', '1', 1)
    print(s)
print(s)