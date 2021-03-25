# 1932

# n = 15
# 7 3 8 8 1 0 2 7 4 4 4 5 2 6 5

#          7                     [0]  
#        3   8                [1]  [2]
#      8   1   0            [3] [4]  [5]
#    2   7   4   4        [6]  [7]  [8]  [9]
#  4   5   2    6   5  [10] [11] [12] [13] [14]

# n >= 1 
#         f(n-1)        
#     f(2n-1)  f(2n)


#          7                                 [0][0]  
#        3   8                          [1][0]     [1][1]
#      8   1   0                  [2][0]     [2][1]     [2][2]
#    2   7   4   4            [3][0]   [3][1]      [3][2]    [3][3]
#  4   5   2    6   5    [4][0]    [4][1]    [4][2]      [4][3]    [4][4] 
#                    [5][0]    [5][1]    [5][2]      [5][3]     [5][4]    [5][5]
triangle = []

n = int(input())

for i in range(n):
    tree = list(map(int, input().split()))    # [['7'],   ['3', '8'],     ['8', '1', '0'],        ['2', '7', '4', '4'],         ['4', '5', '2', '6', '5']]
    triangle.append(tree)       # [0][0]  [1][0] [1][1]  [2][0] [2][1] [2][2]  [3][0] [3][1] [3][2] [3][3]      [4][0] [4][1] [4][2] [4][3]


for i in range (1, n):
    for j in range(len(triangle[i])):

        if j == 0:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j]
        
        elif i == j:
            triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
        
        else:
            triangle[i][j] = max(triangle[i-1][j], triangle[i-1][j-1]) + triangle[i][j]

print(len(triangle))
print(max(triangle[n-1]))

