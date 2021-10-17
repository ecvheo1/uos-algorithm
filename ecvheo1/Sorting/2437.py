import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

sum = 0
for i in arr:
    if i > sum+1:
        break;
    sum += i
print(sum+1)