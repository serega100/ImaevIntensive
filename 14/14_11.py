for base in range(7, 50):
    if int('221', base) + int('34', 8) == int('180', base + 2):
        print(base)
        break