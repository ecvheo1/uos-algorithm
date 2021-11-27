import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF]*(1+n) for _ in range(1+n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, 1+n):
    for a in range(1, 1+n):
        for b in range(1, 1+n):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = INF
for i in range(1, 1+n):
    result = min(result, graph[i][i])

if result == INF:
    print("-1")
else:
    print(result)