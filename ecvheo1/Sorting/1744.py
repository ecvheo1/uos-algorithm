import sys

n = int(sys.stdin.readline())

left = []
right = []
one = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num > 1:
        right.append(num)
    elif num <= 0:
        left.append(num)
    else:
        one.append(num)

right = sorted(right, reverse=True)
left = sorted(left)

result = 0
if len(left) % 2 == 0:
    for i in range(0, len(left), 2):
        result += left[i] * left[i+1]
else:
    for i in range(0, len(left)-1, 2):
        result += left[i] * left[i+1]
    result += left[len(left)-1]

if len(right) % 2 == 0:
    for i in range(0, len(right), 2):
        result += right[i] * right[i+1]
else:
    for i in range(0, len(right)-1, 2):
        result += right[i] * right[i+1]
    result += right[len(right)-1]

result += sum(one)
print(result)