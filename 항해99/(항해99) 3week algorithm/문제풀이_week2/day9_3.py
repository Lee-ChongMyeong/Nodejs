#  11399

n = int(input())
m = list(map(int, input().split()))

m.sort()
total_time = m[0]

for i in range(1,n):
    m[i] += m[i-1]
    total_time += m[i]

print(total_time)