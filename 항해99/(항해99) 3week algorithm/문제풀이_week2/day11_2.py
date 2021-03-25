# 10773

import sys

num = int(sys.stdin.readline())

total_list = []

for i in range(num):
    key = int(sys.stdin.readline())

    if key == 0:
        total_list.pop()
    else:
        total_list.append(key)

print(sum(total_list))