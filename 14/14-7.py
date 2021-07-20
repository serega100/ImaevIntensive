n = 5**2 * 7**25 + 6**2 * 7**36 - 4**2 * 9**3
count = 0

while n > 0:
    if n % 7 == 0:
        count += 1
    n //= 7

print(count)