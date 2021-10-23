import sys

k, n = map(int, sys.stdin.readline().split())
arr = []
for _ in range(k):
    arr.append(int(sys.stdin.readline()))

left = 1
right = max(arr)
while left <= right:
    mid = (left + right) // 2
    sum = 0
    for i in arr:
        sum += i // mid
    if sum < n:
        right = mid - 1
    elif sum >= n:
        result = mid
        left = mid + 1
print(result)