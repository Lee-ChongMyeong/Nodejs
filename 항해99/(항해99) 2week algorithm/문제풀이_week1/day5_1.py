# 4949

while True:
    stack=[];
    push=stack.append  # 데이터를 push (추가)
    pop = stack.pop    # 데이터를 pop  (꺼냄) 
    
    s=input()
    
    if s == '.':
        break

    r='yes'

    for c in s:
        if c in ['[','(']:
            push(c)

        elif c == ']':                          # if stack
            if not stack or pop() != '[':       # 스택에 값이 있을때 -> 참(True)      1
                r='no'                          # 스택에 값이 없을때 -> 거짓(False)    0 
                break
            
        elif c==')':
            if not stack or pop()!='(':
                r='no'
                break

    if stack:
        r='no'

    print(r)
