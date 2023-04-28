# Tutorial
Here is an example of someone using the [AlgoSolver](https://github.com/nickbohm555/AlgoSolver/) library for a competetive programming competition or coding inteerview.

## Prerequisites

Before starting, make sure to run the following:
```
pip install AlgoSolver
```

Also at the top of the file, make sure to import the library.
```
from algo_solver import sorting as sort
from algo_solver import searching as search
from algo_solver import graphs as graph
```

## Example problem Number 1

It is quite common to perform DFS in technical interviews or CP competitions. Here is an example. Find the shortest path between point every point on the graph to point 'F'. Let's say the input is given below:

```
 input_graph = {
            'A': set(['B', 'C']),
            'B': set(['A', 'D', 'E']),
            'C': set(['A', 'F']),
            'D': set(['B']),
            'E': set(['B', 'F']),
            'F': set(['C', 'E']),
        }
find_shortest(input_graph, 'F'):
    return the distance of the shortest path from A to F.
```


## Solution

With AlgoSolver, save time on implementation.

```python
from algo_solver import graphs as graph
find_shortest(input_graph, 'F'):
    # get a list of every key
    for key in input_graph:
        starting = key
        distance = graph.find_distance_unweighted_graph(input_graph, starting , 'F')
        print(distance)
```
  
## Example problem Number 2

It is quite common to perform binary search in technical interviews or CP competitions. Here is an example. Find whether a number 22 exists in a sorted array. We could do this in linear time which would take O(n) time but using bianry search we would save us time to O(logn).

```
input_array = [4, 6, 7, 10, 12, 15, 22, 99, 111, 256, 777]
does_exist(input_array, 22):
    return whether or not 22 exists in the array.
```

## Solution

With AlgoSolver, save time on implementation.

```python
from algo_solver import searching as search
does_exist(input_array, num): 
    index = search.binary_search(input_graph, num)
    if index == -1:
        print('does not exist')
    else:
        print('Exists - found in logn time')
```

## Example problem Number 3

It is quite common to perform sorting operations in technical interviews or CP competitions. Here is an example. Sort an array in O(n) time with the knowledge that the max value is not greater than 50. Here we can perform bucket sort on an array. No need to memorize the implementation.

```
input_array = [33,22,11,21,34,32,19, 23, 39, 1, 4, 6]
```

## Solution

With AlgoSolver, save time on implementation.

```python
from algo_solver import sorting as sort
new_arr = sort.bucket_sort(input_array)
print(new_arr)
```