import sys

n, m = map(int, sys.stdin.readline().split())
aArr, bArr = [], []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    aArr.append(a)
    bArr.append(b)

aArr.sort()
bArr.sort()

sum = 0
mid = m // 2
for i in aArr:
    sum += abs(i-aArr[mid])
for i in bArr:
    sum += abs(i-bArr[mid])
print(sum)