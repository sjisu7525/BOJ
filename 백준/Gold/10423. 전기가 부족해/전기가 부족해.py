n, m, k = map(int, input().split())
power = list(map(int, input().split()))
parent = [ i for i in range(n+1)]
edges = []
for _ in range(m) :
    u, v, w = map(int, input().split())
    edges.append((w,u,v))

def find_p(x) :
    if parent[x] != x :
        parent[x] = find_p(parent[x])
    return parent[x]
def union(a, b):
    a = find_p(a)
    b = find_p(b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

edges.sort()
total = 0
for i in range(1, k) :
    union(power[0], power[i])

for w, u, v in edges :
    if find_p(u) != find_p(v) :
        union(u, v)
        total += w

print(total)
