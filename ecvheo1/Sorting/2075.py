import sys
import heapq

n = int(sys.stdin.readline())
k = []
for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in arr:
        if len(k) < n:
            heapq.heappush(k, j)
        elif k[0] < j:
            heapq.heappop(k)
            heapq.heappush(k, j)
            
print(k[0])
