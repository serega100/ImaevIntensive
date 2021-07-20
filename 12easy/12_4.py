s = '1' * 82
while '1'*5 in s or '888' in s:
    if '1'*5 in s:
        s = s.replace('1'*5, '88', 1)
    elif '888' in s:
        s = s.replace('888', '8', 1)
    print(s, len(s))

print(s)