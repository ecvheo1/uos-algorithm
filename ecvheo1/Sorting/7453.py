import sys
from collections import Counter

n = int(sys.stdin.readline())
arr = [[] for _ in range(4)]
for i in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    arr[0].append(a)
    arr[1].append(b)
    arr[2].append(c)
    arr[3].append(d)

x, y = [], []
for i in range(n):
    for j in range(n):
        x.append(arr[0][i] + arr[1][j])
        y.append(arr[2][i] + arr[3][j])

counter = Counter(y)
sum = 0
for i in x:
    sum += counter[-i]

print(sum)