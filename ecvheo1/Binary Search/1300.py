import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

left = 1
right = n*n

while left <= right:
    mid = (left+right)//2
    count = 0
    for i in range(1, n+1):
        count += min(mid//i, n)
    if count >= k:
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)