import sys
input = sys.stdin.readline
import heapq
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
distance = [1e9]*(n+1)

for _ in range(m) :
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(start)

for num in distance[1:] :
    if num == 1e9 :
        print('INF')
    else :
        print(num)