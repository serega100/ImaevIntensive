for A in range(1, 1000):
    okay = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not ( (not (y**2 <= A) or (y <= 10)) and (not (x <= 9) or (x*x<A))):
                okay = False
                break
        if not okay:
            break
    if okay:
        print(A)