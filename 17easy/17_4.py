def dl(n, d):
    return n % d == 0


count = 0
minn = 11753+1
for n in range(5913, 11753+1):
    if dl(n, 5) and dl(n, 11) and not dl(n, 7) and not dl(n, 10) and not dl(n, 13) and not dl(n, 22):
        count += 1
        minn = min(minn, n)

print(count, minn)