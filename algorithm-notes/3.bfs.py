
graph = [
    [1,4],  #0
    [2,3],  #1
    [3],    #2
    [],     #3
    [4],     #4
]
from collections import deque

def bfs(graph, start):
    visited = set()  # 使用集合记录访问过的节点
    queue = deque([start])  # 使用队列来实现BFS

    while queue:
        vertex = queue.popleft()  # 从队列左侧取出一个节点
        if vertex not in visited:
            visited.add(vertex)  # 标记为已访问
            print(vertex, end=' ')  # 访问节点

            # 将所有未访问的邻居节点添加到队列中
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# 调用BFS
bfs(graph, 0)