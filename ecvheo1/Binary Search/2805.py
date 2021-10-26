import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
left = 0
right = max(tree)

while left <= right:
    mid = (left+right)//2
    sum = 0
    for i in tree:
        if i > mid:
            sum += i - mid
    if sum > m:
        result = mid
        left = mid + 1
    elif sum < m:
        right = mid - 1
    elif sum == m:
        result = mid
        break
print(result)