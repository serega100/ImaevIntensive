# for n in range(400_000_000, 600_000_000+1):
#     x = n
#     while x % 4 == 0:
#         x //= 4
#     while x % 9 == 0:
#         x //= 9
#     if x == 3:
#         print(n, end=' ')
for m in range(2, 31, 2):
    for n in range(1, 20, 2):
        number = (2**m) * (3**n)
        if 400_000_000 <= number <= 600_000_000:
            print(number)