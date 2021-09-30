import sys, copy
from collections import deque


n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus, empty = [], []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i, j))
        if graph[i][j] == 0:
            empty.append((i, j))

def bfs(bg):
    visited = [[False] * m for _ in range(n)] 
    q = deque()
    for i in virus:
        q.append(i)

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and (bg[nx][ny] == 0) and (visited[nx][ny] == False):
                bg[nx][ny] = 2
                q.append((nx, ny))
                visited[nx][ny] = True

    safe = 0
    for i in range(n):
        safe += bg[i].count(0)
    
    return safe

result = []
for i in range(len(empty)):
    for j in range(i):
        for k in range(j):
            graph[empty[i][0]][empty[i][1]] = 1
            graph[empty[j][0]][empty[j][1]] = 1
            graph[empty[k][0]][empty[k][1]] = 1

            bg = copy.deepcopy(graph)
            result.append(bfs(bg))

            graph[empty[i][0]][empty[i][1]] = 0
            graph[empty[j][0]][empty[j][1]] = 0
            graph[empty[k][0]][empty[k][1]] = 0

print(max(result))