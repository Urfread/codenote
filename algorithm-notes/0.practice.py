graph = [
    [1,4],  #0
    [2,3],  #1
    [3],    #2
    [],     #3
    [4],     #4
]

# # 深度优先搜索
# def dfs(graph,start,visited=None):
#     if visited is None:
#         visited=set()
#     visited.add(start)
#     print(f"{start} ->",end=" ")
#     for neighbor in graph[start]:
#         if neighbor not in visited:
#             dfs(graph,neighbor,visited)
# dfs(graph,0)

# 广度优先搜索
from collections import deque
def bfs(graph,start):
    visisted=set()
    queue=deque([start])
    while queue:
        vertex=queue.popleft()
        if vertex not in visisted:
            visisted.add(vertex)
            print(f"{vertex} ->",end=" ")
            for neighbor in graph[vertex]:
                if neighbor not in visisted:
                    queue.append(neighbor)
bfs(graph,0)