# 1037

# A : 5
# N : 20 

# n = int(input())
# divisor = list(map(int, input().split()))
# #print(divisor)

# if n == 1:
#     real_num = divisor[0] * divisor[0]
# else:
#     real_num = divisor[0] * divisor[-1]

# print(real_num)

n = int(input())
a = list(map(int, input().split()))
a_max = max(a)
a_min = min(a)
print(a_max * a_min)