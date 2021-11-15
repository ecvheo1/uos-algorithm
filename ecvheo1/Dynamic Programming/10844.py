import sys
input = sys.stdin.readline

m = 1000000000
n = int(input())
d = [[0 for _ in range(10)] for _ in range(n+1)]
for i in range(1, 10):
    d[1][i] = 1

for i in range(2, n+1):
    for j in range(0, 10):
        if j == 0:
            d[i][j] = d[i-1][1] % m
        elif j == 1:
            d[i][j] = (d[i-1][0] + d[i-1][2]) % m
        elif j == 9:
            d[i][j] = d[i-1][8] % m
        else:
            d[i][j] = (d[i-1][j-1] + d[i-1][j+1]) % m
print(sum(d[n])%m)