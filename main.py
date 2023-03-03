"""main page which includes my functions."""
__author__ = "Nicholas Bohm"
__version__ = "0.1.0"
__license__ = "MIT"

import graphs
import searching
import sorting


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def main():
    """main function which includes my functions."""
    # testable function 1
    print(sorting.radix_sort([15, 3, 222, 11, 8]))

    # testable function 2
    print(searching.selection_algo([15, 3, 222, 11, 8], 1))

    # testable function 3
    print(graphs.bfs(graph, 'A'))

    # testable function 4
    print(graphs.dfs(graph, 'A'))

    # testable function 5
    print(sorting.quick_sort([15, 3, 222, 11, 8]))

    # testable function 6
    print(searching.binary_search([1, 10, 20, 50, 100, 200], 50))

    # testable function 7
    print(sorting.bubble_sort([15, 3, 222, 11, 8]))

    # testable function 8
    print(sorting.bucket_sort([15, 3, 222, 11, 8]))

    # testable function 9
    print(sorting.insertion_sort([15, 3, 222, 11, 8]))

    # testable function 10
    print(sorting.merge_sort([15, 3, 222, 11, 8]))


if __name__ == "__main__":
    main()
