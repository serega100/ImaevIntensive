minn = 99999
maxn = 0
for n in range(2187, 6560+1):
    if (n % 5 != 0) and (n % 7 != 0) and (n % 11 != 0):
        minn = min(minn, n)
        maxn = max(maxn, n)

print(minn, maxn)