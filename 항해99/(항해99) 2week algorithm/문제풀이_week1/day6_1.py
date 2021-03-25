# 2606

# 딕셔너리
# setdefault : 키-값 쌍 추가 / value에 값이 없으면 None이 들어감.
# update = 키의 값 수정, 키가 없으면 키, 값 쌍 추가

com = int(input())    # 7
line = int(input())    # 6
tot = {}
for i in range(com):       
    tot[i+1] = set()    # set() : 빈집합    
                        # set도 딕셔너리 처럼 중괄호를 사용하는데, {}의 경우 딕셔너리로 추론되기 떄문에 set()로 사용
    print(tot)

for i in range(line):
    i,j = map(int,input().split())
    tot[i].add(j)
    tot[j].add(i)
    print(tot)

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            print(visited)
            dfs(i, dic)
            
visited = []

dfs(1,tot)
print(len(visited)-1)


#visited = [False]*(com+1)
#print(visited)

#def dfs(graph,v,visited):
#    visited[v] = True
#    for i in graph[v]:
#        if not visited[i]:
#            dfs(graph,i,visited)
#    return visited

#print(dfs(tot,1,visited).count(True)-1)

