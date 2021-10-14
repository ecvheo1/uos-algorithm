import sys

n = int(sys.stdin.readline())
line = []
for _ in range(n):
    line.append(list(map(int, sys.stdin.readline().split())))
line = sorted(line, key = lambda x : x[0])

start, end = -1000000001, -1000000001
sum = 0
for x, y in line:
    if x >= end:
        sum += end - start
        start = x
        end = y
    elif end < y:
        end = y
sum += (end - start)
print(sum)