n = 4**1014 + 2**1012 - 7
k = 0

while n > 0:
    if n % 2 == 1:
        k += 1
    n //= 2
print(k)