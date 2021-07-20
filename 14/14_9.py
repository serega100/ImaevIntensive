n = 26**2 + 169 - 11
count = 0

while n > 0:
    if (n % 13 == 12) or (n % 13 == 2):
        count += 1
    n //= 13

print(count)