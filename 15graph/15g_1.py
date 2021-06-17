for A in range(-1000, 1000):
    ok = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not ((2*y + 4*x < A) or (x + 2*y > 80)):
                ok = False
                break
        if not ok:
            break
    if ok:
        print(A)