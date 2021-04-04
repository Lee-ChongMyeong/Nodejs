# 1874

n = int(input())
stack = []  # 1 2 3 4 5 6 7 8
op = []     # + + + + + + + + 
count = 1
message = True

for i in range(n):          # n 을 기준으로 n번 반복하는 for문을 돌리면서 num에 입력값을 받는다.
    num = int(input())
    while count <= num:     # num 이 count 보다 작을때 까지 반복:
        stack.append(count) 
        op.append('+')
        count += 1          # count 는 하나씩 증가시키고
        print(stack)        # stack에는 count 값을 축적 
        print(op)           # op 에는 + 를 추가 
    if stack[-1] == num:
        stack.pop()
        op.append('-')
        print(stack)
        print(op)
    else:
        message = False

## 출력

if message == False:
    print('NO')

else:
    for i in op:
        print(i)

# *스택 문제 

# -파이썬 

# push : 데이터를 입력 (append)
# pop : 데이터를 추출 (pop)


# [4, 3, 6, 8, 7, 5, 2, 1]

# + + + + - - + + - + + - - - - -

# [ ] 

# 입력) 
# [stack] 

# 1 2 3 4 	 / + + + +
   
# 1 2 3 4 	 /  
       
# 1 2 5 6	 /

# 1 2 5 7 8 	 /

# 1 2 5 7 8  / 

# 1 2 5	/


# + + + + 	(4까지 쌓임)
# - - 	(4먼저 빠지고 3빠짐 [스택에는 1,2 만 남음])
# + + 	5,6 이 추가됨
# - 	6빠짐
# + + 	7,8이 추가됨
# - - 	8먼저 빠지고 7빠짐
# - - - 	5 -> 2-> 1-> 순으로 빠짐