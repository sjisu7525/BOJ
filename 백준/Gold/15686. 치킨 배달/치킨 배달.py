from itertools import combinations
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
home = [(i,j) for i in range(n) for j in range(n) if arr[i][j] == 1]
chicken = [(i,j) for i in range(n) for j in range(n) if arr[i][j] == 2]

def cal_dist(home, chicken) :
    total_dist = 0
    for i, j in home :
        dist = 1e9
        for ci, cj in chicken :
            dist = min(dist, abs(i-ci) + abs(j-cj))
        total_dist += dist
    return total_dist

answer = 1e9
for c in combinations(chicken, m) :
    answer = min(cal_dist(home, c), answer)

print(answer)