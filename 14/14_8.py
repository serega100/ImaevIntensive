n = 256 ** 2 + 4096 ** 16 - 15
count = 0

while n > 0:
    if n % 16 == 15:
        count += 1
    n //= 16

print(count)
