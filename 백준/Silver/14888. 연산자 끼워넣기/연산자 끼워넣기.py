def cal(a,b,op) :
    if op == "+" :
        return a+b
    elif op == "-" :
        return a-b
    elif op == "*" :
        return a*b
    elif op == "%":
        if a >= 0 :
            return a//b
        else :
            return -((-a)//b)

n = int(input())
num = list(map(int, input().split()))
op_num = list(map(int, input().split())) # 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
op = ["+","-","*","%"]
op_list = []
for o, op_n in zip(op, op_num) :
    op_list += [o]*op_n

from itertools import permutations
min_result = float('inf')
max_result = -float('inf')
for p in set(permutations(op_list, n-1)):
    result = cal(num[0], num[1], p[0])
    for i in range(1,n-1) :
        result = cal(result, num[i+1], p[i])
    min_result = min(min_result, result)
    max_result = max(max_result, result)
print(max_result)
print(min_result)
