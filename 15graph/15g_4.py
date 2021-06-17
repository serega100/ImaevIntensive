for A in range(-1000, 1000):
    ok = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ( (7*y + x < A) or (2*x + 3*y > 98) ):
                ok = False
                break
        if not ok:
            break
    if ok:
        print(A)