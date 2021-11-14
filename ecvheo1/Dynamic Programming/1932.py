import sys
input = sys.stdin.readline

n = int(input())
arr = []
d = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    arr.append(list(map(int, input().split())))

d[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(0, len(arr[i])):
        if j == 0:
            d[i][j] = d[i-1][j] + arr[i][j]
        elif j == n-1:
            d[i][j] = d[i-1][j-1] + arr[i][j]
        else:
            d[i][j] = max(d[i-1][j-1], d[i-1][j]) + arr[i][j]
print(max(d[n-1]))