
N, M = map(int, input().split())

card = list(map(int, input().split())) # 카드 숫자들 리스트

card.sort()

total_number = []
sum = 0
b = len(card)

for i in range(0, b - 2):
    for j in range(i + 1, b - 1):
        for k in range(j + 1, b):
            if card[i] + card[j] + card[k] > M:
                continue
            else:
                sum = max(sum, card[i] + card[j] + card[k])

print(sum)