import sys, heapq

n = int(sys.stdin.readline())
lecture = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lecture.append((a, b))

lecture = sorted(lecture, key = lambda x : x[0])
k = []

for i in range(len(lecture)):
    if k and k[0] <= lecture[i][0]:
        heapq.heappop(k)
    heapq.heappush(k, lecture[i][1])
print(len(k))