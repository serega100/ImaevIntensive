for start in range(-1000, 1000):
    for end in range(-1000, 1000):
        A = range(start, end+1) # [start, end]
        ok = True
        for x in range(-1000, 1000):
            if not ( ((x in A) <= ((x**2) <= 64)) and ((x**2 - 48 <= 2*x) <= (x in A)) ):
                ok = False
                break
        if ok:
            print(start, end)