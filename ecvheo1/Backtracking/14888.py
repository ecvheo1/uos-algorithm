import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
opeartor = list(map(int, sys.stdin.readline().split()))

maximum, minimum = -1e9, 1e9

def check(length, result, plus, minus, multiply, divide):
    global maximum, minimum
    if length == n:
        maximum = max(result, maximum)
        minimum = min(result, minimum)
        return

    if plus:
        check(length+1, result+arr[length], plus-1, minus, multiply, divide)
    if minus:
        check(length+1, result-arr[length], plus, minus-1, multiply, divide)
    if multiply:
        check(length+1, result*arr[length], plus, minus, multiply-1, divide)
    if divide:
        check(length+1, -(-result//arr[length]) if result < 0 else result//arr[length], plus, minus, multiply, divide-1)

check(1, arr[0], opeartor[0], opeartor[1], opeartor[2], opeartor[3])
print(maximum)
print(minimum)