"""graph algorithms."""
from collections import deque
import heapq


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


def djikstras(graph, start):
    """djikstras algorithms."""
    # Initialize the distances and visited sets
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    visited = set()

    # Create a priority queue and add the starting vertex
    priority_queue = [(0, start)]

    while priority_queue:
        # Get the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Ignore visited vertices
        if current_vertex in visited:
            continue

        # Add to visited set
        visited.add(current_vertex)

        # Update the distances for the neighboring vertices
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def bellman_ford():
    """bellman_ford algorithms."""
    print('BellmanFord')


def kruskals():
    """kruskals algorithms."""
    print('Kruskals')


def prims():
    """prims algorithms."""
    print('Prims')


def network_flow():
    """network_flow algorithms."""
    print('NetworkFlow')
