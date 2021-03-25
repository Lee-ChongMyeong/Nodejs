# 2609

# 24(8) : 1 2 3 4 6 8 12 24
# 18(6) : 1 2 3 6 9 18

#  6 |   24    18       // 6
#         4     3       // 72

# 36(9) : 1 2 3 4 6 9 12 18 36
# 28(6) : 1 2 4 7 14 28

#    |    36   28

from collections import Counter

n1, n2 = map(int, input().split())
divisor_n1 = []
divisor_n2 = []

for i in range(1,n1+1):
    if n1 % i == 0:
        divisor_n1.append(i)

for i in range(1,n2+1):
    if n2 % i == 0:
        divisor_n2.append(i)

# print(divisor_n1)
# print(divisor_n2)

ct1 = Counter(divisor_n1)
ct2 = Counter(divisor_n2)

common_min = max(ct1 & ct2)  # 1 2 3 6
print(common_min)           # 최대 공약수
print((n1 // common_min) * (n2 // common_min) * common_min)
#print((n1 * n2) // common_min)