import sys

n = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
budget = int(sys.stdin.readline())

left = 1
right = arr[-1]

while left <= right:
    mid = (left+right)//2
    sum = 0
    for i in arr:
        if i >= mid:
            sum += mid
        else:
            sum += i
    if sum <= budget:
        result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)