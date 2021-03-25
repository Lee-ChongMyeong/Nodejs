# 4673

sum = []
a = []
b = []

def make_con(num):
    
    if num < 10:
        inp2 = int(num) + int(str(num)[0])
        sum.append(inp2)

    elif num < 100:
        inp2 = int(num) + int(str(num)[0]) + int(str(num)[1])
        sum.append(inp2)

    elif num < 1000:
        inp2 = int(num) + int(str(num)[0]) + int(str(num)[1]) + int(str(num)[2])
        sum.append(inp2)


    elif num < 10000: 
        inp2 = int(num) + int(str(num)[0]) + int(str(num)[1]) + int(str(num)[2]) + int(str(num)[3])
        sum.append(inp2)
            
for i in range (1,10001):
    a.append(i)

for i in range(1,10001):
    make_con(i)

for v in a:                 
    if v not in set(sum):
        b.append(v)        

for i in b:
    print(i)


