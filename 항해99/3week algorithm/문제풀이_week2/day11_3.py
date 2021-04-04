# 9012

import sys, time




n = int(sys.stdin.readline())

for i in range (n):
    sum = 0
    
    vps_insert = input()
    vps = list(vps_insert)
    print(vps)
    print(len(vps))

    for i in vps:
        if i == '(':
            sum += 1
    
        elif i == ')':
            sum -= 1

        if sum < 0:
            print('NO')
            break
    
    # if sum == 0:
    #     print('YES')
    # else :
    #     print('NO')
    if sum > 0:
        print('NO')
    elif sum == 0 :
        print('YES')
