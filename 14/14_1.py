for x in range(1, 10000000):
    n = 216**5 + 6**3 - 1 - x
    count = 0
    while n > 0:
        if n % 6 == 5:
            count += 1
        n //= 6
    if count == 12:
        print(x)
        break