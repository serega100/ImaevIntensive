for n in range(1, 100000):
    bn = bin(2*n)[2:]
    bn += str(bn.count('1') % 2)
    bn += str(bn.count('1') % 2)

    if int(bn, 2) > 123:
        print(n)
        break