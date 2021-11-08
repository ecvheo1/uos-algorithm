import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
result = [0, 0, 0]
print(arr)
def check(x, y, n):
    global result
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != color:
                next_n = n // 3
                check(x, y, next_n)
                check(x, y+next_n, next_n)
                check(x, y+2*next_n, next_n)
                check(x+next_n, y, next_n)
                check(x+next_n, y+next_n, next_n)
                check(x+next_n, y+2*next_n, next_n)
                check(x+2*next_n, y, next_n)
                check(x+2*next_n, y+next_n, next_n)
                check(x+2*next_n, y+2*next_n, next_n)
                return
    if color == -1:
        result[0] += 1
    elif color == 0:
        result[1] += 1
    elif color == 1:
        result[2] += 1
    return

check(0, 0, n)
print(result[0])
print(result[1])
print(result[2])