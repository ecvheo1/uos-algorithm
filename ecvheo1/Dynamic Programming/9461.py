import sys
input = sys.stdin.readline

arr = [0] * (101)
arr[1] = 1
arr[2] = 1
arr[3] = 1
arr[4] = 2
arr[5] = 2

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(6, n+1):
        arr[i] = arr[i-1] + arr[i-5]
    print(arr[n])

