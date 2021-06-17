import math

for n in range(102714, 102725+1):
    ds = []
    sq = int(math.sqrt(n))
    if n % sq == 0:
        ds += [sq]
    for d in range(1, sq):
        if n % d == 0:
            ds += [d, n//d]
    if len(ds) == 4:
        print(n)
