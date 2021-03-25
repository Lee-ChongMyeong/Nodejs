# 11050

import sys

total1 = 1
total2 = 1

n1, n2 = map(int,sys.stdin.readline().split())

for i in range(n1 - n2 + 1, n1+1):  # 4, 5
    total1 *= i
for i in range(1, n2+1):            # 1, 2
    total2 *= i

result = total1 // total2 
print(result)

# 5C2
#    5 * 4 
# =  ----------
#    2 * 1

# 2C2
#     2 * 1
# = ---------
#    2 * 1

# 29C13
#   29 * 28 * 27 * 26 * 25 .... 17
# = ----------------------------------
#   13 * 12 * 11 * 10 * 9 * 8 * 7 * 6 ,,, * 2 *1

# from math import factorial

# n,k = map(int, input().split()) 
# print(factorial(n) // (factorial(k) * factorial(n-k)) )