n = 2**102 + 2**100 + 2**85 + 2**17
count = [0] * 8
while n > 0:
    count[n % 8] += 1
    n //= 8
print(count)