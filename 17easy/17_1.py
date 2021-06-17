count = 0
maxn = 0
for n in range(1012, 9638+1):
    if (n % 3 == 0) and (n % 11 != 0) and (n % 13 != 0) and (n % 17 != 0) and (n % 19 != 0):
        count += 1
        maxn = max(maxn, n)

print(count, maxn)