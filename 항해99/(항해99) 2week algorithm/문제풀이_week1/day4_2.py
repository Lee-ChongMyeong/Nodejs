# 11651

num = int(input())
a = []
for i in range(num):
    [x, y] = map(int, input().split())
    rev = [y, x]
    a.append(rev)
b = sorted(a)       # [[-1, 1], [2, 1], [2, 2], [3, 3], [4, 0]]
a.sort()
print(a)

for i in range(num):
    print(b[i][1], b[i][0])


