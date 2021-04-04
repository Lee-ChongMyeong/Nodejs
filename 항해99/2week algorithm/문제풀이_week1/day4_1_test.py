count = int(input())

first_block = []
second_block = []
third_block = []

def hanoi(num):
    tot = 0
    first_block.append(num + 1)
    second_block.append(num + 1)
    third_block.append(num + 1)

    for i in range(1, num + 1):
        tot += i
        first_block.append(i)
        first_block.sort(reverse=True)

    while(sum(third_block) == tot):
        first_block.sort(reverse=True)
        second_block.sort(reverse=True)
        third_block.sort(reverse=True)
        first_block_num = int(len(first_block) -1) 
        second_block_num = int(len(second_block) -1)
        third_block_num = int(len(third_block) -1)
        
        if first_block[first_block_num] < second_block[second_block_num]:
            second_block.append(first_block[first_block_num])

                

        if sum(third_block) == tot:
            break

#    return hanoi(num - 1) * 2 + 1 
hanoi(count)
print(first_block)
print(second_block)
print(third_block)



# 1단 : 1  hanoi(1)
# 2단 : 3  hanoi(1) * 2 + 1
# 3단 : 7  hanoi(2) * 2 + 1
# 4단 : 15 hanoi(3) * 2 + 1
# 5단 : 31 hanoi(4) * 2 + 1

# 3 (2단)

# 1 2 (3)
# 1 3 (4)
# 2 3 (5)

# 7 (3단)
# 1 3  (4)
# 1 2  (3)
# 3 2  (5)
# -----
# 1 3  (4)
# 2 1  (3)
# 2 3  (5)
# -----
# 1 3   (4)

# 15 (4단)
# 1 2    (3)
# 1 3    (4)   
# 2 3    (5)
# -------
# 1 2    (3)
# 3 1    (4)
# 3 2    (5)
# -------
# 1 2    (3)
# 1 3    (4)
# 2 3    (5)
# -------
# 2 1    (3)
# 3 1    (4)
# 2 3    (5)
# -------
# 1 2    (3)
# 1 3    (4)
# 2 3    (5)

# 31 (5단)
# 1 3    (4)
# 1 2    (3)
# 3 2    (5)
# -------
# 1 3    (4)
# 2 1    (3)
# 2 3    (5)
# -------
# 1 3    (4)
# 1 2    (3)
# 3 2    (5)
# -------
# 3 1    (4)
# 2 1    (3)
# 3 2    (5)
# -------
# 1 3    (4)
# 1 2    (3)
# 3 2    (5)
# -------
# 1 3    (4)
# 2 1    (3)
# 2 3    (5)
# -------
# 1 3    (4)
# 2 1    (3)
# 3 2    (5)
# -------
# 3 1    (4)
# 2 1    (3)
# 2 3    (5)
# -------
# 1 3    (4)
# 1 2    (3)
# 3 2    (5)
# -------
# 1 3    (4)
# 2 1    (3)
# 2 3    (5)
# -------
# 1 3    (4)

# 4 1 3 
# ========== 
# 3 1 2 
# 2 1 3 
# 1 1 2 