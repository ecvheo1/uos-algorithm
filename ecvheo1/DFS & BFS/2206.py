import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append([0, 0, 1])
    visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    while q:
        a, b, w = q.popleft()
        if a == n-1 and b == m-1:
            return visited[a][b][w]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if (0 <= nx < n) and (0 <= ny < m):
                if graph[nx][ny] == 1 and w == 1:
                    visited[nx][ny][0] = visited[a][b][w] + 1
                    q.append([nx, ny, 0])
                elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[a][b][w] + 1
                    q.append([nx, ny, w])
    return -1

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

print(bfs())