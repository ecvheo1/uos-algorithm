import sys

n, m = map(int, sys.stdin.readline().split())
arr = [0] * (m+1)

def check(len):
    if len == m+1:
        for i in range(1, m+1):
            print(arr[i], end=' ')
        print()
    else:
        for i in range(1, n+1):
            arr[len] = i
            check(len+1)
check(1)