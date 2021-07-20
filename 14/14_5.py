count = 0
for n16 in range(int('111', 16), int('FFF', 16)+1):
    for digit in range(8):
        n8 = int('4' + str(digit) + '2')
        if n8 == n16:
            count += 1
print(count)