import math

for n in range(81234, 134689+1):
    okay = True
    ds = []
    sq = int(math.sqrt(n))

    if sq*sq == n:
        ds += [sq]
    else:
        continue

    for d in range(2, sq):
        if n % d == 0:
            ds += [d]
            ds += [n//d]


    if len(ds) == 3:
        print(n, ds)
        print(min(ds), max(ds))
