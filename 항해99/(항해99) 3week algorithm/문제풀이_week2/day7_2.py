
# 2839

# 3킬로그램 봉지, 5킬로그램 봉지
# 3A + 5B = N  / 5000kg


N = int(input())
li = [ ]

for a in range(0,1666):
    for b in range(0, 1001):
        if 3*a + 5*b == N:      
            li.append(a+b)  

            
if len(li) == 0:
    print(-1)
else:
    print(min(li))
