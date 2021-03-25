N = int(input())
num = 0
for _ in range(N):
    word = list(input() word:list)
    for i in range(len(word)):
        if i != len(word) - 1:
            if word[i] == word[i+1]:
                pass
            elif word[i] in word[i + 1]:
                break

        else:
            num += 1

print(num)