import sys

n = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))

minValue = 3000000000


for i in range(len(arr)-2):
    left = i+1
    right = len(arr)-1
    while left < right:
        if abs(arr[left] + arr[right] + arr[i]) < minValue:
            minValue = abs(arr[left] + arr[right] + arr[i])
            minPoint = [left, right, i]
        if arr[left] + arr[right] + arr[i] > 0:
            right -= 1
        else:
            left += 1
minPoint.sort()
print(arr[minPoint[0]], arr[minPoint[1]], arr[minPoint[2]])