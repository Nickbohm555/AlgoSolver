from Searching import *
from Sorting import *
from Graphs import *
import unittest


class TestMethods(unittest.TestCase):
    def test_radix(self):
        self.assertEqual(RadixSort([15, 3, 222, 11, 8]), [3, 8, 11, 15, 222])

    def test_selection_algo(self):
        self.assertEqual(SelectionAlgo([15, 3, 222, 11, 8], 1), 8)

    def test_bfs(self):
        graph = {'A': set(['B', 'C']),
                 'B': set(['A', 'D', 'E']),
                 'C': set(['A', 'F']),
                 'D': set(['B']),
                 'E': set(['B', 'F']),
                 'F': set(['C', 'E'])}
        self.assertEqual(Bfs(graph, 'A'), {'A', 'F', 'C', 'B', 'D', 'E'})

    def test_dfs(self):
        graph = {'A': set(['B', 'C']),
                 'B': set(['A', 'D', 'E']),
                 'C': set(['A', 'F']),
                 'D': set(['B']),
                 'E': set(['B', 'F']),
                 'F': set(['C', 'E'])}
        self.assertEqual(Dfs(graph, 'A'), {'A', 'F', 'C', 'B', 'D', 'E'})

    def test_quicksort(self):
        self.assertEqual(QuickSort([15, 3, 222, 11, 8]), [3, 8, 11, 15, 222])

    def test_binary_search(self):
        self.assertEqual(BinarySearch([1, 10, 20, 50, 100, 200], 50), 3)

    def test_bubble_sort(self):
        self.assertEqual(BubbleSort([15, 3, 222, 11, 8]), [3, 8, 11, 15, 222])

    def test_bucket_sort(self):
        self.assertEqual(BucketSort([15, 3, 222, 11, 8]), [3, 8, 11, 15, 222])

    def test_insertion_sort(self):
        self.assertEqual(InsertionSort(
            [15, 3, 222, 11, 8]), [3, 8, 11, 15, 222])


if __name__ == "__main__":
    unittest.main()
