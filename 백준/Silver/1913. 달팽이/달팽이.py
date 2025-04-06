n = int(input())
target = int(input())

d = [(1,0),(0,1),(-1,0),(0,-1)]
start = n*n
arr = [[0]*n for _ in range(n)]
cnt = 0
i, j = 0, 0
k = 0

arr[i][j] = start
while cnt < n*n-1:
    if start == target :
        ti, tj = i+1, j+1
    start -= 1
    if 0 <= i + d[k][0] < n and 0 <= j + d[k][1] < n and arr[i + d[k][0]][j + d[k][1]] == 0 :
        i, j = i + d[k][0], j + d[k][1]
    else :
        k = (k+1) % 4
        i, j = i + d[k][0], j + d[k][1]
    arr[i][j] = start
    cnt += 1
if start == target :
        ti, tj = i+1, j+1

for row in arr :
    print(*row)
print(ti, tj)
