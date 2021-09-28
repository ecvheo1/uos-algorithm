import sys
from collections import deque

def bfs(q, time):
    while q:
        time += 1
        for _ in range(len(q)):
            p = q.popleft()
            if p == k:
                return time
            a, b, c = p-1, p+1, 2*p
            if (0 <= a <= 100000) and graph[a] == 0:
                graph[a] = 1
                q.append(a)
            if (0 <= b <= 100000) and graph[b] == 0:
                graph[b] = 1
                q.append(b)
            if (0 <= c <= 100000) and graph[c] == 0:
                graph[c] = 1
                q.append(c)

n, k = map(int, sys.stdin.readline().split())

graph = [0] * 100001
graph[n] = 1
q = deque()
q.append(n)
time = -1
print(bfs(q, time))