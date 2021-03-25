# 4344

n = int(input())

for i in range(n):
    deq = list(map(int, input().split()))
    a = deq[0]
    score = deq[1:]
    cnt = 0
    avg = sum(score)/a
    for j in score:
        if j > avg:
            cnt += 1
    # ratio = format(cnt/a * 100, .3f)
    print("%.3f%%"%(cnt/a * 100))