mport sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
k = [arr[0]]

for i in range(1, n):
    if k[-1] < arr[i]:
        k.append(arr[i])
    elif k[-1] > arr[i]:
        left = 0
        right = len(k)-1
        while left <= right:
            mid = (left+right)//2
            if k[mid] < arr[i]:
                left = mid + 1
            else:
                right = mid - 1
        k[left] = arr[i]
print(len(k))