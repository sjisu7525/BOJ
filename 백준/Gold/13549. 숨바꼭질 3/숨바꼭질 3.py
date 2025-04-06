import heapq
n, k = map(int, input().split())

def bfs(n, k) :
    dist = [1e9] * 100001
    dist[n] = 0
    q = [(0,n)]

    while q :
        t, x = heapq.heappop(q)
        if x == k :
            print(dist[x])
            return

        if t > dist[x] :
            continue
        
        if 0 <= 2*x < 100001 and dist[2*x] > t :
            dist[2*x] = t
            heapq.heappush(q, (t,2*x))

        for nx in [x-1,x+1] :
            if 0 <= nx < 100001 and dist[nx] > t+1 :
                dist[nx] = t+1
                heapq.heappush(q,(t+1, nx))


bfs(n, k)

