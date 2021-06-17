for A in range(1, 1000):
    ok = True
    for x in range(1, 1000):
        if not (((x & 28 == 0) or (x & 22 == 0)) <= ((x & 56 != 0) <= (x & A == 0))):
            ok = False
            break
    if ok:
        print(A)