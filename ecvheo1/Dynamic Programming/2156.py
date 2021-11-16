import sys
input = sys.stdin.readline

n = int(input())
arr = []
d = [0] * n
for i in range(n):
    arr.append(int(input()))

d[0] = arr[0]

if n > 1:
    d[1] = arr[0] + arr[1]
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+arr[i], d[i-3]+arr[i-1]+arr[i])

print(max(d))