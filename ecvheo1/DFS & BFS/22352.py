import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, sys.stdin.readline().split())
before = []
after = []
for _ in range(n):
    before.append(list(map(int, sys.stdin.readline().split())))
for _ in range(n):    
    after.append(list(map(int, sys.stdin.readline().split())))

def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited = [[False] * m for _ in range(n)]
    visited[a][b] = True
    beforeValue = before[a][b]
    afterValue = after[a][b]
    
    while q:
        x, y = q.popleft()
        before[x][y] = afterValue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and (visited[nx][ny] == False) and (before[nx][ny] == beforeValue):
                visited[nx][ny] = True
                q.appendleft((nx, ny))

def check():
    for i in range(n):
        for j in range(m):
            if before[i][j] != after[i][j]:
                return False
    return True

answer = True
for i in range(n):
    for j in range(m):
        if before[i][j] != after[i][j]:
            bfs(i, j)
            if not check():
                answer = False
if answer:
    print('YES')
else:
    print('NO')
            

