# 1010

#               1
# A             
#               2
# B
#               3
# C
#               4
# D
#               5
# E
#               6

import sys
n = int(input())


for i in range(n):

    total1 = 1
    total2 = 1
    n1, n2 = map(int,sys.stdin.readline().split())

    for i in range(n2 - n1 + 1, n2+1):
        total1 *= i
    for i in range(1, n1+1):
        total2 *= i

    result = total1 // total2 
    print(result)


# print(total1)
# print(total2)



# print(total1)


# <5, 2> 
# 5 * 4    
# 2 * 1

# <5, 1>
# 5 * 1    n * 
# 1 * 1

# <13, 29>

# 29 * 28 * 27 * 26 * 25 * 24 * 23 * 22 * 21 * 20 * 19 * 18 * 17        29  ~ (29 - 13)     
# 13 * 12 * 11 * 10 *  9 *  8 *  7 *  6 *  5 *  4 *  3 *  2 *  1        1 ~ 13