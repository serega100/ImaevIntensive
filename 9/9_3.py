for n in range(2, 100000):
    bn = bin(n)[2:]
    bn = bn[:-1] + bn[1] * 2
    r = int(bn, 2)
    if r > 76:
        print(n)
        break