import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(1+n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

a, b = map(int, input().split())

def dijkstra(start):
    distance = [INF]*(1+n)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

distance_1 = dijkstra(1)
distance_a = dijkstra(a)
distance_b = dijkstra(b)

result = min(distance_1[a]+distance_a[b]+distance_b[n], distance_1[b]+distance_b[a]+distance_a[n])
if result >= INF:
    print('-1')
else: print(result)