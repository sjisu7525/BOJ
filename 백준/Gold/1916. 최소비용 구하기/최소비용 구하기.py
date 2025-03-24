import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
cost = [1e9]*(n+1)

for _ in range(m) :
    s, e, c = map(int, input().split())
    graph[s].append((e,c))

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    cost[start] = 0

    while q :
        pay, now = heapq.heappop(q)
        if pay > cost[now] :
            continue
        for i in graph[now] :
            temp = pay + i[1]
            if temp < cost[i[0]] :
                cost[i[0]] = temp
                heapq.heappush(q,(temp, i[0]))
dijkstra(start)
print(cost[end])