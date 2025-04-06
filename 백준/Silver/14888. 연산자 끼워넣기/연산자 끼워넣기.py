n = int(input())
num = list(map(int, input().split()))
ops = list(map(int, input().split()))
min_val = float('inf')
max_val = -float('inf')

def dfs(depth, total, plus, minus, mul, div) :
    global min_val, max_val
    if depth == n :
        min_val = min(min_val, total)
        max_val = max(max_val, total)
        return

    if plus :
        dfs(depth+1, total+num[depth], plus-1, minus, mul, div)
    if minus :
        dfs(depth+1, total-num[depth], plus, minus-1, mul, div)
    if mul :
        dfs(depth+1, total*num[depth], plus, minus, mul-1, div)
    if div :
        if total >= 0 :
            dfs(depth+1, total//num[depth], plus, minus, mul, div-1)
        else :
            dfs(depth + 1, -((-total)//num[depth]), plus, minus, mul, div - 1)

dfs(1, num[0], *ops)
print(max_val)
print(min_val)