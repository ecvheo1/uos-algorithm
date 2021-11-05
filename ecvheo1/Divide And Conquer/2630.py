import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

result = [0, 0]

def check(x, y, n):
    global result
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                next_n = n//2
                check(x, y, next_n)
                check(x, y + next_n, next_n)
                check(x + next_n, y, next_n)
                check(x + next_n, y + next_n, next_n)
                return
    if color == 0:
        result[0] += 1
    else:
        result[1] += 1
    return

check(0, 0, n)
print(result[0])
print(result[1])