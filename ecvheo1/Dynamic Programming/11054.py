import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

d = [ [1 for _ in range(2)] for _ in range(n) ]
result = 0

for i in range(1, n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            d[i][0] = max(d[i][0], d[j][0]+1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j]:
            d[i][1] = max(d[i][1], d[j][1]+1)

for i in range(n):
    result = max(d[i][0]+d[i][1], result)
print(result-1)