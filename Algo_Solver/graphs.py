"""graph algorithms."""
from collections import deque


def bfs(graph, start):
    """bfs algorithms."""
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

    return visited


def dfs(graph, start):
    """dfs algorithms."""
    visited = set()

    def dfs_helper(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start)
    return visited
