import sys
from collections import Counter

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

k = Counter(card)
for i in num:
    print(k[i], end=" ")