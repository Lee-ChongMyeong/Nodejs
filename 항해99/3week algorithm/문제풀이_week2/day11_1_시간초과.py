
# 10828

import sys
num = int(sys.stdin.readline())

stack_list = []

def stack_result(string):
    if string == 'push':
        stack_list.append(n[1])
        
    elif string == 'top':
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list[-1])

    elif string == 'size':
        print(len(stack_list))

    elif string =='empty':
        if len(stack_list) >= 1:
            print(0)
        else:
            print(1)
    
    elif string == 'pop':
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list[-1])
            stack_list.pop()

for i in range(num):       
    n = sys.stdin.readline().split() 
    stack_result(n[0])

