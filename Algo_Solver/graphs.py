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
    queue = deque([(start, 0)])
    
    while queue:
        vertex, distance = queue.popleft()
        
        if vertex not in visited:
            visited.add(vertex)
            
            if vertex == end:
                return distance
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    d[neighbor] = distance + 1
                    queue.append((neighbor, distance + 1))  # Add neighbor with its distance from start
    return -1  # We have explored the entire graph and did not find the destination


def count_values(head):
    """
    Counts the number of times each value appears in a linked list.

    Args:
        head (ListNode): The head node of the linked list.

    Returns:
        dict: A dictionary with keys as values in the linked list and values as the count of occurrences.
    """
    counts = {}
    curr = head
    while curr:
        if curr.val not in counts:
            counts[curr.val] = 1
        else:
            counts[curr.val] += 1
        curr = curr.next
    return counts
=======
                    queue.append((neighbor, distance + 1))
    
    return -1


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

import heapq

def dijkstra(graph, start):
    """
    Computes the shortest path to every node in a graph using Dijkstra's Algorithm.

    Args:
        graph (dict): The graph we are traversing.
        start (int): The starting node to find shortest paths from.

    Returns:
        dict: A dictionary containing the shortest distance to each node from the starting node.
    """
    
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    
    queue = [(0, start)]

    while queue:
        
        current_distance, current_node = heapq.heappop(queue)

        
        if current_distance > distance[current_node]:
            continue

       
        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

    return distance

def topological_sort(graph):
    """
    Sorts a directed acyclic graph in topological order.

    Args:
        graph (dict): The directed acyclic graph to sort.

    Returns:
        list: The nodes of the graph in topological order.
    """
    in_degrees = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degrees[neighbor] += 1

    queue = []
    for node in in_degrees:
        if in_degrees[node] == 0:
            queue.append(node)

    top_order = []
    while queue:
        node = queue.pop(0)
        top_order.append(node)
        for neighbor in graph[node]:
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)

    return top_order
