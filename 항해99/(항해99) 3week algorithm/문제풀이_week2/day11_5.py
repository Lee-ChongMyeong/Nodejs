# 1260

import sys, time
from collections import deque



# [1,2] 
# [1,3]
# [1,4]
# [2,4]
# [3,4]

m, n, start =  map(int,sys.stdin.readline().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(graph, start, visited):
    visited[start] = True

    print(start, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문

    for i in range(1, m+1):
        if not visited[i] and graph[start][i] == 1:
            dfs(graph, i, visited)

visited = [False] * (n+1)

dfs(graph, start, visited)

print()


# def bfs(graph, start, visited2):
#     queue = deque([start])
#     visited2[start] = True

#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')

#         for i in graph[v]:
#             if not visited2[i]:
#                 queue.append(i)
#                 visited2[i] = True

# visited2 = [False] * (n + 1)

# bfs(graph, start, visited2)