a = int('46', 8)
b = int('40', 16)
c = int('47', 8) - int('1B', 16)
d = int('110101', 2) + int('13', 8)

x = 3 * 16**a + 5 * 4**b - 8**c - 2**d + 15
print(hex(x).count('f'))