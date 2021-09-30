import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):

    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    q = deque()
    q.append((x,y))
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and (island[nx][ny] == 'L') and (visited[nx][ny] == 0):
                visited[nx][ny] = visited[a][b] + 1
                q.append((nx, ny))
    return visited[a][b]-1

n, m = map(int, sys.stdin.readline().split())
island = []

for _ in range(n):
    island.append(list(sys.stdin.readline().rstrip()))

allResult = []
for i in range(n):
    for j in range(m):
        if island[i][j] == 'L':
            allResult.append(bfs(i, j))
print(max(allResult))