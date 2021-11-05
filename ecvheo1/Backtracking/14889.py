import sys
input = sys.stdin.readline

def dfs(count, start):
    global minValue
    if count == n//2:
        start = 0
        link = 0
        linkTeam = []
        for i in range(n):
            if i not in startTeam:
                linkTeam.append(i)

        for i in range(n//2):
            for j in range(i+1, n//2):
                    start += arr[startTeam[i]][startTeam[j]] + arr[startTeam[j]][startTeam[i]]
                    link += arr[linkTeam[i]][linkTeam[j]] + arr[linkTeam[j]][linkTeam[i]]

        minValue = min(abs(start-link), minValue)
        return
    
    for i in range(start, n):
        if visited[i]:
            continue
        visited[i] = True
        startTeam[count] = i
        dfs(count+1, i+1)
        visited[i] = False
        
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

startTeam = [0] * (n//2)
visited = [False] * n
minValue = 1e9

dfs(0, 0)
print(minValue)