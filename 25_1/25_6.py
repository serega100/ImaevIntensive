found = []
for n in range(1395, 22717+1):
    sn = str(n)
    okay = True
    for i in range(len(sn)-1):
        if not (sn[i] <= sn[i+1]):
            okay = False
            break

    if okay:
        found += [n]

print(found)
print(sum(found))