# Graphs
<!-- Short summary or background information -->
A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

Here is some common terminology used when working with Graphs:

- Vertex - A vertex, also called a “node”, is a data object that can have zero or more adjacent vertices.
- Edge - An edge is a connection between two nodes.
- Neighbor - The neighbors of a node are its adjacent nodes, i.e., are connected via an edge.
- Degree - The degree of a vertex is the number of edges connected to that vertex.


## Challenge
<!-- Description of the challenge -->
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

- add node
    Arguments: value
    Returns: The added node
    Add a node to the graph
- add edge
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing
    Adds a new edge between two nodes in the graph
    If specified, assign a weight to the edge
    Both nodes should already be in the Graph
- get node
    Arguments: none
    Returns all of the nodes in the graph as a collection (set, list, or similar)
- get neighbors
    Arguments: node
    Returns a collection of edges connected to the given node
    Include the weight of the connection in the returned collection
- size
    Arguments: none
    Returns the total number of nodes in the graph

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
add node: O(1) time/space
add edge: O(1) time/space
get node: O(n) time/space
get neighbors: O(n) time/space
size: O(1) time/space
`__str__`: O(n) time/space


## API
<!-- Description of each method publicly available in your Graph -->

- add node method that takes in value as argument and returns added node

- add edge method that takes in 2 nodes as arguments as well as the weight (optional) and returns nothing

- get node method that takes in no arguments and returns all nodes in the graph as a collection (set, list, or similar)

- get neighbors method that takes in a node as argument and returns all edges of the given node as a collection (set, list, or similar)

- size method that takes in no arguments and returns the total number of nodes in the graph
- `__str__` representation of the graph as a string


- [x] created Node class
- [x] created Graph class
- [x] created add node
- [x] created add edge
- [x] created get node
- [x] created get neighbors
- [x] created size
- [x] created `__str__`
