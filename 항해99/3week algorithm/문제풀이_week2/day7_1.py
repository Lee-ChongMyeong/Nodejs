# 1316

# 1. 각각 다른 알파벳  -> 자동으로 그룹 단어
# 2. 알파벳 입력 간 중간에 똑같은 알파벳이 -> 그룹 단어가 될수 있고 안될 수도 있다.     ex) abbc, abbcb 
# 3. 똑같은 알파벳이 나중에 다시 나올 때. ex) abca, bcdebb

N = int(input())
group = []      # 입력한 문자 넣는 곳
check = [a, b,  ]      # 원소들 넣는 곳
cnt = 0         # 그룹 단어 개수 카운트

for i in range(0,N):    # i = 0, 1, 2, ... N-1
    s = input()
    group.append(s)

# group= [['happy'], ['new'], ['year']]     
# happy = group[0][0]
# new = group[0][1]
# year = group[0][2]

    print(group)


    for j in range(0,len(group[i])):        # len(group[0] = 5)
        if group[i][j] not in check:        # 'h' = group[0][0], 'a' = group[0][1], 'p' = group[0][2], 'p' = group[0][3] 'y' = group[0][4]
            check.append(group[i][j])       #  a b a b   / check [ a, b]   
            print(check)
            continue

        elif group[i][j] in check:
            if group[i][j] == check[-1]:
                check.append(group[i][j])
                continue
            else:           # 이때는 check []에 수가 안들어가게 됨.
                break

    if len(check) == len(group[i]):         # 그룹단어일때 check 수랑, 입력 숫자랑 같게 됨.
        cnt += 1               

    check = []  

print(cnt)
    
