import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
d = [x for x in arr]

print(d)
for i in range(1, n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            d[i] = max(d[i], d[j] + arr[i])

print(d)