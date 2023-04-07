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


def find_distance_unweighted_graph(graph, start, end):
    """
    Performs breadth first search on a graph with a given starting point to find the distance to end.

    Args:
        graph (dict): The graph we are traversing.
        start (int): The starting node to traverse from.
        end (int): The destination we are trying to reach.

    Returns:
        int: The distance from start to end of an unweighted graph.
    """
    visited = set()
    d = {}
    d[start] = 0
    queue = deque([(start, 0)])  # Store each node with its distance from the start
    while queue:
        vertex, distance = queue.popleft()
        if vertex == end:
            return distance  # We have reached the destination
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    d[neighbor] = distance + 1
                    queue.append((neighbor, distance + 1))  # Add neighbor with its distance from start
    return -1  # We have explored the entire graph and did not find the destination
