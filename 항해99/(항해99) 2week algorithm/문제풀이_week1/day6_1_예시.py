# 변수 선언 및 입력을 받기위한 코드
number_of_computers = int(input()) #컴퓨터의 수
number_of_connected_computers = int(input()) #적접 연결된 컴퓨터 쌍의 수
number_of_pair_computers = [] #직접 연결되어 있는 컴퓨터의 번호쌍
reversed_number_of_pair_computers=[] #그 것을 거꾸로 돌린거

for i in range(number_of_connected_computers): # 직접 연결되어 있는 컴퓨터의 쌍을 입력받기 위한 처리
    com1, com2 = map(int, input().split())
    number_of_pair_computers.append([com1, com2])

for i in number_of_pair_computers: # 위의 처리의 나온 결과를 반대로 해주는 처리 ex)[[2,3]] => [[3,2]]
    reversed_number_of_pair_computers.append([i[1],i[0]])


# 연결쌍의 컴터를 딕셔너리 타입으로 바꾸기 위한 함수
def generate_hash(n, array): #매개변수는 컴퓨터의 수와, 직접 연결 쌍의 배열
    keys = list(range(1, n+1)) #키로 사용하기 위해 컴퓨터의 수를 받아서 리스트로 만든다
    tree={} 
    tmp = []    #array =[[1,2], [1,3], [2,3]...] 
    for i in keys:     
        for j in array: #연결쌍의 첫번째 인덱스가 키와 일치할 때 tmp배열에 넣어준다
            if i == j[0]:
                tmp.append(j[1])
               
        else:
            tree[i] = tmp #두 번이 나왔을 때의 처리
            tmp = []    
                                
    return tree 

tree1 = generate_hash(number_of_computers, number_of_pair_computers)  
print(tree1)         
tree2 = generate_hash(number_of_computers, reversed_number_of_pair_computers)           

def two_in_one (n,dict1, dict2): #DFS, BFS를 위해 딕셔너리 타임으로 바꾼 연결쌍, 리버스연결쌍을 합치는 함수
    real_tree = {}
    keys = list(range(1, n+1))
    for i in keys:
        real_tree[i] = dict1[i] + dict2[i]
        real_tree[i].sort()
    return real_tree    

total_tree = two_in_one(number_of_computers, tree1, tree2) 

def infected_computers(total_tree, start_node): #DFS를 하는 함수
    visited = []
    stack = [start_node]
    while stack:
        current_node = stack.pop()
        visited.append(current_node)
        for adjacent_node in total_tree[current_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)
    return list(set(visited))

print(len(infected_computers(total_tree, 1))-1)