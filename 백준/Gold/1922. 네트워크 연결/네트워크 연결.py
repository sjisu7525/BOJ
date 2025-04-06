import heapq
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def prim(start, graph, v) :
    q = [(0,start)]
    visited =  [False]*(v+1)
    total = 0

    while q :
        cost, node = heapq.heappop(q)
        if visited[node] :
            continue
        visited[node] = True
        total += cost

        for n_cost, n_node in graph[node] :
            if not visited[n_node] :
                heapq.heappush(q, (n_cost, n_node))
    return total

print(prim(1, graph, n))