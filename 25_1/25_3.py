import math

max_count = 0
max_n = 0
max_ds = []
for n in range(286564, 287270+1):
    ds = []
    sq = int(math.sqrt(n))
    if n % sq == 0:
        ds += [sq]
    for d in range(1, sq):
        if n % d == 0:
            ds += [d, n//d]
    if len(ds) >= max_count:
        max_count = len(ds)
        max_n = n
        max_ds = ds

max_ds.sort()
max_ds.reverse()
print(max_count, max_ds[:2])
