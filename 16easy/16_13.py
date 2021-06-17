def F(n):
    if n <= 3:
        return n
    elif n % 2 == 0:
        return n + 3 + F(n-1)
    else:
        return n * n + F(n-2)

count = 0
for n in range(1, 1000+1):
    if F(n) % 7 == 0:
        count += 1

print(count)