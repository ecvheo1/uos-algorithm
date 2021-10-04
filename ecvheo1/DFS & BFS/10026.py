import sys
from collections import deque


def bfsNo(a, b, visitedNo):
    q = deque()
    q.append((a, b))
    visitedNo[a][b] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < n) and (visitedNo[nx][ny] == False) and (paint[nx][ny] == paint[x][y]):
                visitedNo[nx][ny] = True
                q.append((nx, ny))

n = int(sys.stdin.readline())
paint = []
for _ in range(n):
    paint.append(list(sys.stdin.readline().rstrip()))

resultNo = 0
resultYes = 0
visitedNo = [[False] * n for _ in range(n)]
visitedYes = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

for i in range(n):
    for j in range(n):
        if visitedNo[i][j] == False:
            bfsNo(i, j, visitedNo)
            resultNo += 1

for i in range(n):
    for j in range(n):
        if paint[i][j] == 'G':
            paint[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if visitedYes[i][j] == False:
            bfsNo(i, j, visitedYes)
            resultYes += 1

print(resultNo, resultYes)