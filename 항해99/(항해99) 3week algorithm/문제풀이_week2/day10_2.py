# 1934

def LCM(A,B):
    d = GCD(A,B)
    return int((A*B) / d)

def GCD(A,B):
#    return GCD(B%A, A) if B%A else A
    if B%A == 0:
        return A
    else:
        return GCD(B%A, A)

# 24 % 18  = 6
# 18 % 6 = 0    --> else A

T = int(input())

for i in range(T):
    A,B = map(int, input().split())
    print(LCM(A,B))
