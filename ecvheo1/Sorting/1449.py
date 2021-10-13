import sys

n, l = map(int, sys.stdin.readline().split())
water = sorted(list(map(int, sys.stdin.readline().split())))
k = [0 for _ in range(1001)]

sum = 0
x = 0
for i in water:
    if x < i:
        x = i + (l-1)
        sum += 1 

print(sum)