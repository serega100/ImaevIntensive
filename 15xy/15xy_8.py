count = 0
for A in range(-1000, 1000):
    ok = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not ( (not (y*y<16) or (y <= A)) and (not (x <= A) or (x * x <= 100)) ):
                ok = False
                break
        if not ok:
            break
    if ok:
        print(A)
        count += 1

print('Кол-во:', count)