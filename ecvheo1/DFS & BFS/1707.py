import sys
from collections import deque

color = 1

def bfs(x):
    q = deque([x])
    visited[x] = color
    global isBiparitite
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = visited[x] * -1
                q.append(i)
            if (visited[i] + visited[x]) != 0:
                isBiparitite = False
                return

t = int(sys.stdin.readline())

for _ in range(t):
    v, e = map(int, sys.stdin.readline().split())
    
    graph = [[] for _ in range(v+1)]
    for i in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0] * (v+1)
    isBiparitite = True

    for i in range(1, v+1):
        if(not isBiparitite):
            break
        if(visited[i] == 0):
            bfs(i)
    
    if isBiparitite: print('YES')
    else: print('NO')