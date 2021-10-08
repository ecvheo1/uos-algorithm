import sys
import heapq

n = int(sys.stdin.readline())

lecture = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lecture.append((a, b))

lecture = sorted(lecture, key = lambda x : x[1])

k = []
sum  = 0
for i in range(10000, 0, -1):
    if lecture and lecture[len(lecture)-1][1] == i:
        while lecture and lecture[len(lecture)-1][1] == i:
            a, b = lecture.pop()
            heapq.heappush(k, (-a, b))
        a, b = heapq.heappop(k)
        sum += -a
    else:
        if k:
            a, b = heapq.heappop(k)
            sum += -a
        
print(sum)