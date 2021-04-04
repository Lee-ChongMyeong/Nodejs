# 2108

from collections import Counter
import sys

total_list = []

n = int(sys.stdin.readline())
for i in range (n):    
    m = int(sys.stdin.readline())   
    total_list.append(m)
    
total_list.sort()
print(total_list[0])

total_list_frequency = Counter(total_list).most_common()

def frequency(total_list):
    if len(total_list) > 1:
        if total_list[0][1] == total_list[1][1]:
            print(total_list[1][0])
        else:
            print(total_list[0][0])
    else:
        print(total_list[0])

sansul = sum(total_list) // len(total_list) 
center_number = total_list[len(total_list)//2]
cover =  max(total_list) - min(total_list)

print(sansul)
print(center_number)
frequency(total_list_frequency)
print(cover)