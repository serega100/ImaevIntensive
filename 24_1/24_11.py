file = open('k8-69.txt')
s = file.readline()

symb = ''
k = 0
max_symb = ''
max_k = 0

for i in range(len(s)-1):
    k += 1
    if s[i] == s[i+1]:
        if symb == '':
            symb = s[i]
    else:
        if k > max_k:
            max_k = k
            max_symb = symb
        k = 0
        symb = ''

print(max_symb, max_k)