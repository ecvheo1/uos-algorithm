import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def pow(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        x = pow(a, b//2)
        return x * x % c
    else:
        x = pow(a, (b-1)//2)
        return a * x * x % c
    
value = pow(a, b)
print(value)