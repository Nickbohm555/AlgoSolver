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


if __name__ == "__main__":
    unittest.main()
