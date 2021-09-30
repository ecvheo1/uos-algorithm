import sys
from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

t = int(sys.stdin.readline())
for _ in range(t):
    move = 0
    n = int(sys.stdin.readline())
    graph = [[0] * n for _ in range(n)]
    a, b = map(int, sys.stdin.readline().split())
    lastA, lastB = map(int, sys.stdin.readline().split())
    
    q = deque()
    q.append((a, b))
    graph[a][b] = 0
    while q:
        x, y = q.popleft()
        if x == lastA and y == lastB:
            print(graph[x][y])
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))