def F(x, y, z):
    return int(not (z or y) or (x == z))


for x in range(2):
    for y in range(2):
        for z in range(2):
            if F(x, y, z) == 0:
                print(y, z, x, F(x, y, z))