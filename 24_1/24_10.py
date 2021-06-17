file = open('k7c-3.txt')
s = file.readline()

count = 0
for i in range(len(s)-2):
    if s[i] == s[i+2] and s[i+1] in ['B', 'D', 'E'] and s[i+2] in ['A', 'C', 'D'] and s[i+1] != s[i+2]:
        count += 1

print(count)