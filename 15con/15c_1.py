for A in range(1, 1000):
    ok = True
    for x in range(1, 1000):
        if not (not (x&A !=0) or (not (x&44==0) or (x&76 != 0))):
            ok = False
            break
    if ok:
        print(A)