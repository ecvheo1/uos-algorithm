import sys
import heapq
from collections import deque

n, k = map(int, sys.stdin.readline().split())

jewel = []
bag = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    jewel.append((a, b))

for _ in range(k):
    bag.append(int(sys.stdin.readline()))

jewel = sorted(jewel, key = lambda x : (x[0], -x[1]))
bag.sort()

k = []
sum = 0
j = 0
for i in bag:
    while j < n and i >= jewel[j][0]:
        heapq.heappush(k, (-jewel[j][1], jewel[j][1]))
        j += 1
    if k:
        sum += heapq.heappop(k)[1]
print(sum)