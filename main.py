
__author__ = "Nicholas Bohm"
__version__ = "0.1.0"
__license__ = "MIT"
import Dp
import Graphs
import Searching
import Sorting
import NumberTheory

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def main():
    # testable function 1
    print(Sorting.RadixSort([15,3,222,11,8]))

    # testable function 2
    print(Searching.SelectionAlgo([15,3,222,11,8], 1))
    
    # testable function 3
    print(Graphs.Bfs(graph, 'A'))

    # testable function 4
    print(Graphs.Dfs(graph, 'A'))

    # testable function 5
    print(Sorting.QuickSort([15,3,222,11,8], 1))
    """ Main entry point of the app """
    
    


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()