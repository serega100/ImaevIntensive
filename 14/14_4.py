max_sum = 0
the_base = 0
for base in range(2, 10+1):
    n = 2345
    summ = 0
    while n > 0:
        summ += n % base
        n //= base
    if summ > max_sum:
        max_sum = summ
        the_base = base
print(the_base)