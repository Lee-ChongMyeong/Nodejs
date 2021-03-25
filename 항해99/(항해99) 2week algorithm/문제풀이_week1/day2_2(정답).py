input = list(range(1 , 10001)) #1부터 10000까지의 리스트

'''
밑의 함수는 셀프넘버를 찾기 위한 함수다.
파이썬은 문자를 리스트 형식으로 사용 할 수가 있다.
그래서 인자를 문자형으로 바꾼후 다시 숫자형으로 변환하는 과정을 마치면 인자의 각 자릿수가 존재하는 리스트가 나오게된다.
그 리스트의 합과, 인자를 더해서 리턴한다.

ex)
generateSelfNum(123)
=> 123 을 '123'으로 str(n)
=> '123'을 [1,2,3]으로 list(map(lambda x : int(x), str(n)))
=> 123 + (1+2+3)을 리턴
'''
def generateSelfNum(n):
    return n + sum(list(map(lambda x : int(x), str(n))))

# print(generateSelfNum(1))
'''
그런 다음 , 1부터 10000까지 돌면서
앞에서 만들어 놓은 함수에 대입을 시키고,
함수의 리턴값이 앞에서 선언한 1부터 10000까지의 리스트에 존재하면 해당 숫자를 삭제한다.
'''
for i in range(1, len(input)+1):
    if generateSelfNum(i) in input:
        input.remove(generateSelfNum(i))
    else:
        pass
'''
그 다음 남은 값을 하나씩 출력해준다.
'''
tmp = []
for i in input:
    # print(i)       
    tmp.append(i) 
print(len(tmp))       
# selfNum(input)