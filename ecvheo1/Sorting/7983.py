import sys

n = int(sys.stdin.readline())
work = []
for _ in range(n):
    work.append(list(map(int, sys.stdin.readline().split())))

work = sorted(work, key = lambda x : x[1], reverse=True)

now = work[0][1] - work[0][0]
result = 0

for i in range(1, n):
    if now <= work[i][1]:
        now = now - work[i][0]
    else:
        now = work[i][1] - work[i][0]

print(now)