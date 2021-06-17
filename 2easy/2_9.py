def F(x, y, z, w):
    return int(((not y or z) or (not x and w)) == (w == z))


for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if F(x, y, z, w) == 1:
                    print(z, w, y, x, F(x, y, z, w))