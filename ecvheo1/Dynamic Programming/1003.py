import sys
input = sys.stdin.readline

zero = [1, 0, 1]
one = [0, 1, 1]

def fibo(n):
    if len(zero) <= n:
        for i in range(len(zero), n+1):
            zero.append(zero[i-2]+zero[i-1])
            one.append(one[i-2]+one[i-1])
    print(zero[n], one[n])


t = int(input())
for _ in range(t):
    fibo(int(input()))