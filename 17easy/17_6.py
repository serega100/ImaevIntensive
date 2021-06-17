def dl(n, d):
    return n % d == 0


minn = 9285+1
maxn = 0
for n in range(1812, 9285+1):
    if (dl(n, 8) or dl(n, 19)) and not dl(n, 4) and not dl(n, 9) and int(str(n)[0]) % 2 != 0:
        minn = min(minn, n)
        maxn = max(maxn, n)


print(minn, maxn)