file = open('26-k3.txt')
n, k, m = map(int, file.readline().split())
scores = list(map(int, file.readlines()))
scores.sort()
scores.reverse()

print(scores[k+m-1], scores[k-1])