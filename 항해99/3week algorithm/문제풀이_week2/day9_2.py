# 11047

n, m = map(int, input().split())
money_list = []
count = 0

# M= 4200

for i in range(n):
    money = int(input())
    money_list.append(money)
    money_list.sort(reverse=True)
# [1, 5, 10, 50, 100, 500 ... ]
# [50000, 10000, 5000, 1000, 500, 100 ]
#print(money_list)

for i in money_list:
    count += m//i   
#    print(count)
    m %= i      
#    print(m)
print(count)
