def find_p(x) :
    if parent[x] != x :
        parent[x] =  find_p(parent[x])
    return parent[x]
def union(a,b) :
    a = find_p(a)
    b = find_p(b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n = int(input())
m = int(input())
parent = [ i for i in range(n+1)]
edges = []
for _ in range(m) :
    a,b,c = map(int, input().split())
    edges.append((c,a,b))
edges.sort()
total = 0
for c, a, b  in edges:
    if find_p(a) != find_p(b) :
        union(a,b)
        total += c
print(total)
