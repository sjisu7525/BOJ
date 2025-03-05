from collections import deque

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
id = 1
c = []
for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 1 :
            id += 1
            arr[i][j] = id
            q = deque([(i,j)])
            cnt = 1
            while q :
                ci, cj = q.popleft()
                for di, dj in [(1,0),(-1,0),(0,1),(0,-1)] :
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1 :
                        arr[ni][nj] = id
                        cnt += 1
                        q.append((ni,nj))
            c.append(cnt)

print(id-1)
c.sort()
for i in c :
    print(i)