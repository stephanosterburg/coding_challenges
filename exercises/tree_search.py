from collections import deque

# breadth first search
def bfs(graph, root):
    visited, queue = set(), deque([root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
print(bfs(graph, 0))

# depth first search
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)

    return visited


graph = {
    "0": set(["1", "2"]),
    "1": set(["0", "3", "4"]),
    "2": set(["0"]),
    "3": set(["1"]),
    "4": set(["2", "3"]),
}

print(dfs(graph, "0"))
