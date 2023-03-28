"""main page which includes my functions."""
__author__ = "Nicholas Bohm"
__version__ = "0.1.0"
__license__ = "MIT"

import graphs
import searching
import sorting


graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E']),
}


def main():
    """main function which includes my functions."""


if __name__ == "__main__":
    main()
