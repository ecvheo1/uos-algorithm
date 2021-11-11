import sys
input = sys.stdin.readline

arr = [[[-1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def w(x, y, z):
    
    if x <= 0 or y <= 0 or z <= 0:
        return 1
    
    if x > 20 or y > 20 or z > 20:
        return w(20, 20, 20)
    
    if arr[x][y][z] != -1:
        return arr[x][y][z]
    
    if x < y and y < z:
        arr[x][y][z] = w(x, y, z-1) + w(x, y-1, z-1) - w(x, y-1, z)
        return arr[x][y][z]
    
    cal =  w(x-1, y, z) + w(x-1, y-1, z) + w(x-1, y, z-1) - w(x-1, y-1, z-1)
    arr[x][y][z] = cal
    return cal

while(1):
    x, y, z = map(int, input().split())

    if x == -1 and y == -1 and z == -1:
        exit()
    print( f'w({x}, {y}, {z}) = {w(x, y, z)}' )