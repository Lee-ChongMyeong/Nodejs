
# 1. 만약 메모에 있으면 그 값을 바로 반환하고
# 2. 없으면 아까 수식대로 구한다.
# 3. 그리고 그 값을 다시 메모에 기록한다.

# 딕셔너리안의 key 값을 튜플로 받을 수 있다!

memo = {}

def met(a,b,c, memo):

    if (a,b,c) in memo.keys():       # 1 
        return memo[(a,b,c)]

    if a <= 0 or b <= 0 or c <= 0:   # 2 
        return 1

    elif a > 20 or b >20 or c > 20:     # 3 
        memo[(20, 20, 20)] = w(20,20,20, memo)
        return memo[(20, 20, 20)]

    elif a < b and b < c:               # 4 
        memo[(a,b,c)] = w(a, b, c-1, memo) + w(a, b-1, c-1, memo) - w(a, b-1, c, memo)
        return memo[(a,b,c)]

    else:   # 5 
        memo[(a,b,c)] = w(a-1, b, c, memo) + w(a-1, b-1, c, memo) + w(a-1, b, c-1, memo) - w(a-1, b-1, c-1, memo)
        return memo[(a,b,c)]

while True:
    x,y,z = map(int, input().split())
    if x == -1 and y == -1 and z == -1:
        break
    print(f'w({x}, {y}, {z}) = {met(x,y,z, memo)}')