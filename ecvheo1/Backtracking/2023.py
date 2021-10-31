import sys

input = sys.stdin.readline
n = int(input())
arr = [0] * n

def isPrimeNumber(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def checkAmazingPrimeNumber(len):
    if len == n:
        for i in range(n):
            print(arr[i], end='')
        print()
        return

    for i in range(1, 10):
        arr[len] = i
        x = arr[0]
        for j in range(1, len+1):
            x = x*10 + arr[j]
        if isPrimeNumber(x):
            checkAmazingPrimeNumber(len+1)
        else:
            arr[len] = 0

checkAmazingPrimeNumber(0)