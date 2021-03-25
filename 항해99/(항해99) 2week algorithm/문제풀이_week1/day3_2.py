# 10250

t = int(input())

for i in range(t):
    h, w, n=map(int,input().split())

    # 호수 구하기
    line =  n // h+1

    # 사람수가 층수로 나누어질때
    if n%h == 0:
        floor = h
        line = n // h
    else:
        floor = n%h
    
    answer = floor * pow(10,2) + line
    print(answer)