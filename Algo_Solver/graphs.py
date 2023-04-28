"""
These API's provides utilities for graph algorithms.

Functions:
 `bfs`: Retrieved every element reachable from starting point using bfs technique.

 `dfs`: Retrieved every element reachable from starting point using dfs technique.

"""

from collections import deque


def bfs(graph, start):
    """
    Performs breadth first search on a graph with a given starting point.

    Args:
        graph (dict): The graph we are traversing.
        start (int): The starting node to traverse from.

    Returns:
        set: The set of all nodes we visit.
    """
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

    return visited


def dfs(graph, start):
    """
    Performs depth first search on a graph with a given starting point.

    Args:
        graph (dict): The graph we are traversing.
        start (int): The starting node to traverse from.

    Returns:
        set: The set of all nodes we visit.
    """
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
        int: The distance fom start to end of an unweighted graph.
    """
    visited = set()
    queue = deque([start])
    dist = {}
    # testing to see if works
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
            dist[vertex] = dist.get(vertex, 0) + 1
            if vertex == end:
                return dist[vertex]
    return -1
