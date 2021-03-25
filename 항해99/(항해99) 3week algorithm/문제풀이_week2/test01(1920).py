import sys, time
start_time = time.time() # 측정시작

first_number = int(sys.stdin.readline())
first_list = set(map(int, sys.stdin.readline().split()))
second_number = int(sys.stdin.readline())
second_list = list(map(int, sys.stdin.readline().split()))

for i in second_list:
    if i in first_list:
        print(1)
    else:
        print(0)

end_time = time.time() # 측정 종료
print("time : ", end_time - start_time)