import sys


r, c, k = map(int, sys.stdin.readline().split())
graph = [[0] * 101 for _ in range(101)]
n, m = 3, 3

def solve():
    global n, m
    for time in range(101):
        if graph[r][c] == k:
            print(time)
            return
        if n >= m:
            for i in range(1, n+1):
                cnt = [0] * 101
                for j in range(1, m+1):
                    if graph[i][j]:
                        cnt[graph[i][j]] += 1
                        graph[i][j] = 0
                b = []
                for j in range(1, 101):
                    if cnt[j]:
                        b.append((cnt[j], j))
                b.sort()
                m = max(m, len(b)*2)
                j = 1
                for x in b:
                    graph[i][j+1], graph[i][j] = x
                    j += 2
        else:
            for i in range(1, m+1):
                cnt = [0]  * 101
                for j in range(1, n+1):
                    if graph[j][i]:
                        cnt[graph[j][i]] += 1
                        graph[j][i] = 0
                b = []
                for j in range(1, 101):
                    if cnt[j]:
                        b.append((cnt[j], j))
                b.sort()
                n = max(n, len(b)*2)
                j = 1
                for x in b:
                    graph[j+1][i], graph[j][i] = x
                    j += 2
    print(-1)
                    

for i in range(1, 4):
    graph[i][1], graph[i][2], graph[i][3] = map(int, sys.stdin.readline().split())

solve()