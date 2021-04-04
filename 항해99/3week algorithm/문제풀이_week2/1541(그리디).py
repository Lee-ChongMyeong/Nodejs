
# 55 + 40 + 20 - 60 - 200 - 10 + 30 - 70


arr = input().split('-')
# ['50+40+20', '60', '200', '10+30', '70']

print(arr)
s = 0
for i in arr[0].split('+'):
    print(i, end=' ')
    s += int(i)

print()

for i in arr[1:]:
    for j in i.split('+'):
        print(j, end=' ')
        s -= int(j)

print(s)
