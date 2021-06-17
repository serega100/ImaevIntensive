for A in range(0, 1000):
    ok = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ( (y + 5*x != 80) or (3*x > A) or (y > A)):
                ok = False
                break
        if not ok:
            break
    if ok:
        print(A)