for i in range(100, 1000):
    digits = list(map(int, list(str(i))))
    sum1 = digits[0] + digits[1]
    sum2 = digits[1] + digits[2]
    if (sum1 == 11 and sum2 == 17) or (sum1 == 17 and sum2 == 11):
        print(i)
        break
