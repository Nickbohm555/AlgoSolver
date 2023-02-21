from collections import deque
import heapq

def Bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

    return visited

def Dfs(graph, start):
    visited = set()

    def dfs_helper(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start)
    return visited

def Djikstras(graph, start):
    # Initialize the distances and visited sets
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    visited = set()

    # Create a priority queue and add the starting vertex
    pq = [(0, start)]

    while pq:
        # Get the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(pq)

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
                heapq.heappush(pq, (distance, neighbor))

    return distances

def BellmanFord():
    print('BellmanFord')

def Kruskals():
    print('Kruskals')

def Prims():
    print('Prims')

def NetworkFlow():
    print('NetworkFlow')