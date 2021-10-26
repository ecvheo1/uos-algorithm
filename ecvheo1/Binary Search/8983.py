import sys

m, n, l = map(int, sys.stdin.readline().split())
hunt = sorted(list(map(int, sys.stdin.readline().split())))
animal = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    animal.append((x, y))
animal = sorted(animal, key = lambda x : x[0])

sum = 0
for x,y in animal:
    left = 0
    right = m-1
    while left < right:
        mid = (left + right) // 2
        if x > hunt[mid]:
            left = mid+1
        else:
            right = mid
    if abs(hunt[right]-x)+y <= l or abs(hunt[right-1]-x)+y <= l:
        sum += 1
print(sum)