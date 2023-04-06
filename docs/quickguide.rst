Quick Guide
======================================

AlgoSolver allows developers to implement useful algorithms as a black box.


Overview
------------
My goal is to develop a library in python to help programmers solve a variety of algorithms style questions. For example, with Dynamic Programming problems the main things we need to know are if we are using a 1D of 2D array, what the base case is, and what the recurrence relation is. With this in mind, we can create multiple templates for different types of questions to take out the implementation process. I wanted to have a special focus on graph algorithms for the library. This will allow programmers to spend more of their time thinking about high level design questions.

Installation
------------
To install, run the following:

>>> pip install ppip install AlgoSolver

Usage
======================================

Sorting
------------
The following code will sort an array for you using merge sort and return the sorted array .  

`arr`: An array you are searching through. 

>>> from algo_solver import sorting as s
arr = s.merge_sort(arr = [1,5,3,2])
print(arr)


Searching
------------
The following code will find the index of a given number 'num' in an array 'arr' .  

`arr`: An array you are searching through. 
`num`: A number you are searching for.

>>> from algo_solver import searching as s
index = s.binary_search(arr = [1,5,3,2], num = 3)
print(index)

Graphs
------------

The following code will give a set of all nodes in the graph through bfs. It is given a graph 'graph' and starting point 'start'.

`graph`: A Graph you are traversing through. 

`start`: The Node of the graph you are searching from.

>>> from algo_solver import graphs as g
index = g.bfs(graph = {2: [3], 3: []} start = 2)
print(index)

