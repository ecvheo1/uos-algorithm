import sys

n = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

for i in num:
    flag = False
    left = 0
    right = n-1
    while left <= right:
        mid = (left+right) // 2
        if i < arr[mid]:
            right = mid-1
        elif i > arr[mid]:
            left = mid+1
        elif i == arr[mid]:
            flag = True
            break
    if flag: print(1)
    else: print(0)