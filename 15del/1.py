def dl(x, n):
    return x % n == 0


for A in range(1, 1000):
    ok = True
    for x in range(1, 1000):
        if not (dl(x, A) or not dl(x, 21) or dl(x, 14)):
            ok = False
            break
    if ok:
        print(A)