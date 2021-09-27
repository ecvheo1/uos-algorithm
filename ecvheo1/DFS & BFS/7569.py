import sys
from collections import deque

def bfs(q, time):
    while q:
        time += 1
        for _ in range(len(q)):
            z, x, y = q.popleft()
            for i in range(6):
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]
            
                if (0 <= nz < h) and (0 <= nx < n) and (0 <= ny < m) and (box[nz][nx][ny] == 0):
                    box[nz][nx][ny] = 1
                    q.append((nz, nx, ny))
    return time


m, n, h = map(int, sys.stdin.readline().split())
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append((i, j, k))

dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

time = -1
time = bfs(q, time)

for i in range(h):
    for j in range(n):
        if box[i][j].count(0) > 0:
            time = -1
            break

print(time)