import sys

n, t = map(int, sys.stdin.readline().split())

carrot = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
carrot.sort(key = lambda x:(x[1], x[0]))

sum = 0
for i in range(n-1, -1, -1):
    sum += carrot[-1][0] + carrot[-1][1] * (t-n+i)
    carrot.pop()
print(sum)