import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
x = []

for i in range(n-1):
    x.append(arr[i+1] - arr[i])
x.sort()

sum = 0
for i in range(n-k):
    sum += x[i]
print(sum)