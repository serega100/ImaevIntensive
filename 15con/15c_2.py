for A in range(1, 1000):
    ok = True
    for x in range(1, 1000):
        if not ((x & A != 0) <= ((x & 29 == 0) <= (x & 86 != 0))):
            ok = False
            break
    if ok:
        print(A)
