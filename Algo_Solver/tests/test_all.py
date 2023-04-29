"""testing page."""
import unittest
import sys

sys.path.append('../')
from AlgoSolver.Algo_Solver.searching import *
from AlgoSolver.Algo_Solver.sorting import *
from AlgoSolver.Algo_Solver.graphs import *


# importing


class TestMethods(unittest.TestCase):
    """class to test all methods."""

    def test_radix(self):
        """testing radix_sort."""
        self.assertEqual(radix_sort([15, 3, 222, 11, 8]), [3, 8, 11, 15, 222])

    def test_selection_algo(self):
        """testing selection_sort."""
        self.assertEqual(selection_algo([15, 3, 222, 11, 8], 1), 8)

    def test_bfs(self):
        """testing bfs."""
        graph = {
            'A': set(['B', 'C']),
            'B': set(['A', 'D', 'E']),
            'C': set(['A', 'F']),
            'D': set(['B']),
            'E': set(['B', 'F']),
            'F': set(['C', 'E']),
        }
        self.assertEqual(bfs(graph, 'A'), {'A', 'F', 'C', 'B', 'D', 'E'})

    def test_dfs(self):
        """testing dfs."""
        graph = {
            'A': set(['B', 'C']),
            'B': set(['A', 'D', 'E']),
            'C': set(['A', 'F']),
            'D': set(['B']),
            'E': set(['B', 'F']),
            'F': set(['C', 'E']),
        }
        self.assertEqual(dfs(graph, 'A'), {'A', 'F', 'C', 'B', 'D', 'E'})

    def test_quicksort(self):
        """quicksort test."""
        self.assertEqual(quick_sort([15, 3, 222, 11, 8]), [3, 8, 11, 15, 222])

    def test_binary_search(self):
        """binary search test."""
        self.assertEqual(binary_search([1, 10, 20, 50, 100, 200], 50), 3)

    def test_bubble_sort(self):
        """bubble sort test."""
        self.assertEqual(bubble_sort([15, 3, 222, 11, 8]), [3, 8, 11, 15, 222])

    def test_bucket_sort(self):
        """bucket sort test."""
        self.assertEqual(bucket_sort([15, 3, 222, 11, 8]), [3, 8, 11, 15, 222])

    def test_insertion_sort(self):
        """insertin sort test."""
        self.assertEqual(insertion_sort([15, 3, 222, 11, 8]), [3, 8, 11, 15, 222])

    def test_bfs_dfs_integration(self):
        """insertin sort test."""
        # Create a sample graph to test the integration between bfs and dfs
        graph = {
            'A': set(['B', 'C']),
            'B': set(['A', 'D', 'E']),
            'C': set(['A', 'F']),
            'D': set(['B']),
            'E': set(['B', 'F']),
            'F': set(['C', 'E']),
        }

        # Run a bfs search on the graph
        bfs_result = bfs(graph, 'A')

        # Run a dfs search on the graph
        dfs_result = dfs(graph, 'A')

        # Check that the bfs and dfs searches return the same set of nodes
        self.assertEqual(bfs_result, dfs_result)

    def test_find_distance_unweighted_graph(self):
        """find_distance_unweighted_graph test."""

        graph = {
            'A': set(['B', 'C']),
            'B': set(['A', 'D', 'E']),
            'C': set(['A', 'F']),
            'D': set(['B']),
            'E': set(['B', 'F']),
            'F': set(['C', 'E']),
        }
        self.assertEqual(find_distance_unweighted_graph(graph, 'A', 'F'), 2)

    def test_dijkstra(self):
        """Testing Dijkstra's Algorithm."""
        graph = {
            'A': {'B': 3, 'C': 1},
            'B': {'A': 3, 'C': 7, 'D': 2},
            'C': {'A': 1, 'B': 7, 'D': 1},
            'D': {'B': 2, 'C': 1},
        }
        expected_output = {'A': 0, 'B': 3, 'C': 1, 'D': 2}
        self.assertEqual(dijkstra(graph, 'A'), expected_output)

    def test_linear_search(self):
        """Testing linear search."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(linear_search(arr, 5), 4)

    def test_find_duplicates(self):
        """Testing find_duplicates."""
        arr4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
        self.assertEqual(find_duplicates(arr4), [10])

    def test_is_palindrome(self):
        """Testing test_is_palindrome."""
        self.assertTrue(is_palindrome("racecar"))

    def test_two_pointer_sort(self):
        """Testing two_pointer_sort."""
        arr1 = [1, 3, 5, 7, 9]
        arr2 = [2, 4, 6, 8, 10]
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(two_pointer_sort(arr1, arr2), expected_result)

    def test_topological_sort(self):
        graph = {'A': ['C', 'D'], 'B': ['D', 'E'], 'C': ['F'], 'D': ['F'], 'E': ['G'], 'F': ['G'], 'G': []}
        self.assertEqual(topological_sort(graph), ['A', 'B', 'C', 'D', 'E', 'F', 'G'])

    def test_heapsort(self):
        """Testing heapsort."""
        arr = [5, 2, 8, 3, 9, 1]
        expected_result = [1, 2, 3, 5, 8, 9]
        heapsort(arr)
        self.assertEqual(arr, expected_result)

    def test_count_values(self):
        """Testing count_values."""

        class Node:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next

        # create a linked list with values 1 -> 2 -> 1 -> 3 -> 2 -> 1 -> None
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(1)
        head.next.next.next = Node(3)
        head.next.next.next.next = Node(2)
        head.next.next.next.next.next = Node(1)

        # create the expected dictionary
        expected_result = {1: 3, 2: 2, 3: 1}

        # count the values in the linked list
        result = count_values(head)

        # compare the expected and actual results
        self.assertDictEqual(result, expected_result)

    def test_bellman_ford(self):
        """Testing Bellman-Ford algorithm."""
        graph = {'A': {'B': -1, 'C': 4}, 'B': {'C': 3, 'D': 2, 'E': 2}, 'C': {}, 'D': {'B': 1, 'C': 5}, 'E': {'D': -3}}
        start = 'A'
        expected_result = {'A': 0, 'B': -1, 'C': 2, 'D': -2, 'E': 1}
        result = bellman_ford(graph, start)
        self.assertDictEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
