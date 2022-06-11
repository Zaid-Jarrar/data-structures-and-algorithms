


class Node:
    """
    Node class:
    - self.value: node value
    """
    def __init__(self,value):
        self.value=value
    
class Edge:
    """
    Edge class:
    - node: Node
    - weight: int
    """
    def __init__(self,node,weight=0):
        self.node=node
        self.weight=weight


    
class Graph:
    """
    Graph class:
    - adjacency_list: dict
    has the following methods:
    - add_node(value)
    - add_edge(node_1, node_2, weight=0)
    - get_node()
    - get_neighbors(node)
    - size()
    - __str__()
    """

    def __init__(self):
        self.adjacency_list = {}
        

    def add_node(self, value): 
        """
        Arguments: value
        Returns: The added node
        Add a node to the graph        
        """     

        node = Node(value)
        self.adjacency_list[node] = []
        return node

    def add_edge(self, node_1, node_2, weight=0):
        """             
            Arguments: 2 nodes to be connected by the edge, weight (optional)
            Returns: nothing
            Adds a new edge between two nodes in the graph
            If specified, assign a weight to the edge
            Both nodes should already be in the Graph
        """
        if not (node_1 in self.adjacency_list.keys()) or not (node_2 in self.adjacency_list.keys()):
            raise KeyError("One or more of the nodes is not in the graph")
        else:
            edge = Edge(node_2, weight=weight)
            self.adjacency_list[node_1].append(edge)


    def get_node(self):
        """ 
        Arguments: none
        Returns all nodes in graph as a collection (set, list, or similar)
        
        """
        output=[]
        for node in self.adjacency_list.keys():
            output.append(node.value)
        return output


    def get_neighbors(self, node):
        """              
            Arguments: node
            Returns a collection of edges connected to the given node
            Include the weight of connection in returned collection           
        """
        if not (node in self.adjacency_list.keys()):
            raise KeyError("The node is not in the graph")
        else:
            output=[]
            for edge in self.adjacency_list[node]:
                output.append([edge.node.value,edge.weight])
            return output
       

    def size(self):
        """         
        Arguments: none
        Returns the total number of nodes in the graph
        """
        return len(self.adjacency_list)

    def __str__(self):
        output = ''
        for node in self.adjacency_list.keys():
            output += f"{node.value} -> "

            for edge in self.adjacency_list[node]:
                output += f' {edge.node.value} ->'
            
            output += ' Null\n'
        return output
        


if __name__ == '__main__':
    graph = Graph()
    a=graph.add_node('A')
    b=graph.add_node('B')
    c=graph.add_node('C')
    d=graph.add_node('D')
    e=graph.add_node('E')
    f=graph.add_node('F')
    g=graph.add_node('G')
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(a, d)
    graph.add_edge(b, e)
    graph.add_edge(b, f)
    graph.add_edge(c, g)


    print(graph.get_node())
        

