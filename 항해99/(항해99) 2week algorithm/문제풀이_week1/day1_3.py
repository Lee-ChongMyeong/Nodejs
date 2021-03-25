# 2884

a, b = input().split()

a = int(a)
b = int(b)

c = int((a * 60) + b - 45)

d = int(c / 60)
e = c % 60

if c > 0:
    c = int((a * 60) + b - 45)
    print( int(c / 60), int(c % 60))
elif c ==0:
    print(0, 0)
elif c < 0:
    c = ((a + 24) * 60 + b) - 45
    print( int(c / 60), int(c % 60))