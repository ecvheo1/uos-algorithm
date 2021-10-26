import sys

n, c = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()

left = 1
right = arr[n-1] - arr[0]

while left <= right:
    mid = (left+right)//2
    count = 1
    current = arr[0]
    for x in arr:
        if current + mid <= x:
            count += 1
            current = x
    if count >= c:
        left = mid + 1
        result = mid
    else:
        right = mid - 1
print(result)