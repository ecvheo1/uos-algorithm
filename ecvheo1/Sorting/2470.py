import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

left = 0
right = len(arr)-1
minValue = 2000000000


while left < right:
    if minValue > abs(arr[left] + arr[right]):
        minValue = abs(arr[left] + arr[right])
        minPoint = (left, right)
    if arr[left] + arr[right] > 0:
        right -= 1
    else:
        left += 1
print(arr[minPoint[0]], arr[minPoint[1]])