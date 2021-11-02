n = int(input())

count = 0
board = [0] * n
visited = [False] * n

def check(x):
    for i in range(x):
        if (x - i) == abs(board[x] - board[i]):
            return False
    return True

def queen(x):
    global count
    if x == n:
        count += 1
        return
    for i in range(n):
        if not visited[i]:
            board[x] = i
            if check(x):
                visited[i] = True
                queen(x+1)
                visited[i] = False            

queen(0)
print(count)