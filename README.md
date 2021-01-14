Welcome to the OOP_Ex3 wiki!

# Ex3 - Graphs In Python

## Introduction

In this project, we developed infrastructure of data structure and algorithms on a weighted, directed graph in Python.

A weighted graph is a graph in which each edge is given a numerical weight.

A directed graph is a set of objects (called vertices or nodes) that are connected together, where all the edges are directed from one vertex to another.

This project is combination of Ex2 project and Python. 



## First part
At the beginning, we did NodeData class which describe the features of vertex in the graph.
Then, we did DiGraph class which implements GraphInterface. In this class, we make functions such as:

## DiGraph Class


| Method  | Description |
------------|----------------
|`v_size()`|Returns the number of vertices in the graph
|`e_size()`|Returns the number of edges in the graph
|`get_all_v()`|Return a dictionary of all the nodes in the Graph, each node is represented using a pair (key, node_data)
|`all_in_edges_of_node(id1)`|Return a dictionary of all the nodes connected to (into) node_id, each node is represented using a pair (key, weight)
|`all_out_edges_of_node(id1)`|Return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key, weight)
|`get_mc()`|Returns the current version of the graph, on every change in the graph state - the MC should be increased
|`add_edge(id1, id2, weight)  `        | Adds an edge with a weight between two nodes to the graph |
| `add_node(node_id, pos)  `                |    Adds a node to the graph                                         
`remove_node(node_id)`|Removes a node and all the edges which starts or ends at this node from the graph
|`remove_edge(node_id1, node_id2) ` |  Removes an edge between two nodes from the graph
|`get_node()` | Returns the node associated with the graph (a given key)



## Second part
We did GraphAlgo class that implements GraphAlgoInterface (which represent a collection of algorithms on graphs). In this class, we make functions such as:

## GraphAlgo Class


| Method  | Description |
------------|----------------
|`get_graph()`|Returns the directed graph on which the algorithm works on
|`load_from_json(file_name)`| Loads a graph from a json file
|`save_to_json(file_name)`|  Saves the graph in JSON format to a file
|`shortest_path(id1, id2)`|Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm. Returns the distance of the path and a list of the nodes ids that the path goes through
|`connected_component(id1)`| Finds the Strongly Connected Component(SCC) that node id1 is a part of
|`connected_components()`|Finds all the Strongly Connected Component(SCC) in the graph. This methos is using the `connected_component(id1)` function to get.
|`plot_graph() `     |  Plots the graph. If the nodes have a position, the nodes will be placed there. Otherwise, they will be placed in a random but elegant manner. This method is using matplotlib.pyplot (a comprehensive library for creating static, animated, and interactive visualizations in Python).|



## Third part
We compared between this project, Ex2 and NetworkX (data structures for graphs, digraphs, and multigraphs).

The comparison included the following components:
1. Correctness check
2. Comparative test of runtime on scenarios - with an emphasis on algorithms

We compared the following functions:

`shortest_path()`

`connected_component()`

`connected_components()`

