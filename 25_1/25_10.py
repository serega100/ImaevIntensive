def dels_count(n):
    count = 1
    d = 2
    while d * d < n:
        if n % d == 0:
            count += 2
        d += 1
    if d * d == n:
        count += 1
    return count


found = []

for n in range(1000000, 1300000+1):
    okay = True
    digits = list(map(int, list(str(n))))
    for digit in digits:
        if digit >= 3:
            okay = False
            break

    if not okay:
        continue

    if sum(digits) % 10 == 0:
        found += [[n, dels_count(n)]]

for i in range(len(found)//10):
    index = 9 + 10 * i
    print(found[index][0], found[index][1], end=' ')