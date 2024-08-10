# 假设我们有一个图，节点从0到3，边如下：
# 0 -> 1
# 1 -> 2
# 2 -> 0, 3
# 3 -> 3
graph = [
    [1],  # 节点0与节点1相连
    [2],  # 节点1与节点2相连
    [0, 3], # 节点2与节点0和节点3相连
    [3]   # 节点3与自身相连
]
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # 使用集合记录访问过的节点

    visited.add(start)  # 标记起始节点为已访问
    print(start, end=' ')  # 访问起始节点

    # 遍历与当前节点相连的所有节点
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # 递归访问未访问过的邻居节点

# 调用DFS
dfs(graph, 0)