# 1002

# 조규현 x1, y1
# 백승환 x2, y2
# 류재명 x3, y3
# 류재명 거리 : r1(x1,y1 ~) /  r2(x2, y2 ~ )



t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    rs = r1 + r2
    rm = abs(r1 - r2)

    if d == 0:          # 두 원이 일치하는 경우
        if r1 == r2:
            print(-1)
        else:
            print(0)

    else:
        if d == rs or d == rm:      # 두 원이 한점에서 만나는 경우
            print(1)
        elif d < rs and d > rm:     # 두 원이 만나지 않는 경우
            print(2)
        else:
            print(0)

