for A in range(0, 1000):
    ok = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ((5*y + 4*x > A) or (2*x + 3*y < 90) or (y - 2*x < - 150)):
                ok = False
                break
        if not ok:
            break
    if ok:
        print(A)