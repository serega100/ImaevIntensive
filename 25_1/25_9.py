import math

for n in range(321654, 654321+1):
    max_d = 0
    count_ds = 0

    okay = True
    sq = int(math.sqrt(n))
    for d in range(2, sq):
        if n % d == 0:
            if d % 2 != 0 and (n//d) % 2 != 0:
                count_ds += 2
                max_d = max(max_d, n//d)
            else:
                okay = False
                break

    if not okay:
        continue

    if sq * sq == n:
        if sq % 2 != 0:
            count_ds += 1
            max_d = max(max_d, sq)
        else:
            continue

    if count_ds > 70:
        print(n, max_d, end=' ')