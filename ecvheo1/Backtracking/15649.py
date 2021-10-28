import sys

n, m = map(int, sys.stdin.readline().split())
arr = [0] * (m+1)
visit = [False] * (n+1)

def isNotDepulicate(x):
    if visit[x]:
        return True
    else:
        return False

def check(len):
    if len == m+1:
        for i in range(1, m+1):
            print(arr[i], end=" ")
        print()
    else:
        for i in range(1, n+1):
            if not isNotDepulicate(i):
                visit[i] = True
                arr[len] = i
                check(len+1)
                visit[i] = False

check(1)