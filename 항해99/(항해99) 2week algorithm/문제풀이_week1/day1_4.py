# 1110

count = 0
a = input()
target = a
while True:
    count +=1
    b = 0
    if int(a) < 10:
        c = '0'+str(a)
        b = (int(a)%10)*10 + int(c[1])
    else:
        c = (int(a)//10) + int(a)%10
        if c < 10:
            b = (int(a)%10)*10 +  c
        else:
            b = (int(a)%10)*10 + c%10
    if int(target) != b:
        a = str(b)
        continue
    
    elif int(target) == int(b):
        print(count)      
        break