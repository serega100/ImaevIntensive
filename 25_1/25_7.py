def is_unique(n):
    digits = list(map(int, list(str(n))))
    return (digits[2] % 2 == 0) and (digits[4] % 2 == 0) and (digits[0] % 2 != 0) and (digits[1] % 2 != 0) and (digits[3] % 2 != 0)


count = 0
minn = None
maxn = 0
for n in range(33333, 55555+1):
    if is_unique(n) and (n % 6 != 0) and (n % 7 != 0) and (n % 8 != 0):
        count += 1
        if minn is None:
            minn = n
        maxn = n

print(count, maxn-minn)
# 2346 22092