import sys
input = sys.stdin.readline

n = int(input())
k = []

for _ in range(n):
    k.append(list(map(int, input().split())))
k.sort(key = lambda x : x[0])

arr = [x[1] for x in k]
d = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            d[i] = max(d[i], d[j]+1)
print(n-max(d))