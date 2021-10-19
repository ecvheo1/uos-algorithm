import sys

n = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
x =  int(sys.stdin.readline())

left = 0
right = len(arr)-1
sum = 0
while left < right:
    if arr[left] + arr[right] == x:
        sum += 1
        right -= 1
        left += 1
    elif arr[left] + arr[right] > x:
        right -= 1
    elif arr[left] + arr[right] < x:
        left += 1
print(sum)