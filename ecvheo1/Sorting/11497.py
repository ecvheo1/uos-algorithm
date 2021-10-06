import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    tree = list(map(int, sys.stdin.readline().split()))
    tree.sort()
    treeFront = tree[::2]
    if n % 2 == 1:
        tree.pop()
    treeRear = tree[n::-2]
    tree = treeFront + treeRear

    diff = abs(tree[1] - tree[0])
    for i in range(1, n):
        if i == n-1:
            diff = max(diff, abs(tree[i]-tree[0]))
        else:
            diff = max(diff, abs(tree[i+1]-tree[i]))
    print(diff)