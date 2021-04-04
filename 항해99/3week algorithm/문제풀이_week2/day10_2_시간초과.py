# 1934

import sys
from collections import Counter     # Counter 라이브러리

def divison_result(n1, n2): # 최소 공배수 만든는 함수 정의

    divisor_n1 = []     # n1 약수가 들어감
    divisor_n2 = []     # n2 약수가 들어감

    for i in range(1,n1+1):
        if n1 % i == 0:
            divisor_n1.append(i)       # divisor_n1 에 n1의 약수가 들어감

    print(divisor_n1)
    for i in range(1,n2+1):
        if n2 % i == 0:
            divisor_n2.append(i)        # divisor_n2에 n2의 약수가 들어감
    print(divisor_n2)

    ct1 = Counter(divisor_n1)
    ct2 = Counter(divisor_n2)
    
    common_min = max(ct1 & ct2)         # 최대 공약수

    print((n1 * n2) // common_min)      # 최소 공배수      
                                                                
n = int(input())                                                

for i in range(n):
    n1, n2 = map(int,sys.stdin.readline().split())
    divison_result(n1, n2)