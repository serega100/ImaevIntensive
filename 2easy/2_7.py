def F(x, y, z, w):
    return int(((not y or x) or (not z and w)) == (x == w))


for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if F(x, y, z, w) == 1:
                    print(x, w, y, z, F(x, y, z, w))