# 9184

import sys
input = sys.stdin.readline

def w(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)


    if dp[a][b][c] :            # 값이 이미 존재한다면 그 값을 바로 리턴
        return dp[a][b][c]

    if a<b<c :
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)

    else:
        dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)

    print(dp[a][b][c])
    return dp[a][b][c]  
    



dp = [[[0 for _ in range(21)] for _ in range (21)] for _ in range (21)]

# 입력값이 abc 세개 이기 때문에 범위를 3차 배열로 형성
# dp 테이블에는 각 계산값이 담기는 형태로 들어간다.

while True:

    a,b,c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c)))

#  if dp[a][b][c] : return dp[a][b][c] 즉 dp[a][b][c]의 값이 존재한다면, 해당 값을 리턴하라는 기능만 추가해주면
# 연산 속도가 기하급스적으로 빨라진다.