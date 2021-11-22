import sys
input = sys.stdin.readline

arr1 = list(input().rstrip())
arr2 = list(input().rstrip())
len1 = len(arr1)
len2 = len(arr2)

d = [[0 for _ in range(len2+1)] for _ in range(len1+1)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if arr1[i-1] == arr2[j-1]:
            d[i][j] = d[i-1][j-1]+1
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])

print(d[-1][-1])