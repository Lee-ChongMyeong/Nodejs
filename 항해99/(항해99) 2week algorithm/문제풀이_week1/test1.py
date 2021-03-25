
user_card_num = int(input())
user_card = set(map(int, input().split()))
system_card_num = int(input())
system_card = list(map(int, input().split()))

# 리스트는 인덱스 0부터 N까지 일일이 검사해야하므로
# 시간 복잡도가 O(n) 이고, set은 O(1) 이다.

for i in range(system_card_num):        
    if system_card[i] in user_card:
        print(1, end = " ")
    else:
        print(0, end=" ")