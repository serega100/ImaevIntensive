def F(x, y, z, w):
    return int((not x or z) and (not z or w) or (y == (x or z)))


for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if F(x, y, z, w) == 0:
                    print(y, z, w, x, F(x, y, z, w))