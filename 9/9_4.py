for n in range(1, 100000):
    bn = bin(n)[2:]
    if n % 2 == 0:
        bn += '00'
    else:
        bn += '11'
    r = int(bn, 2)

    if r < 102:
        print(n)