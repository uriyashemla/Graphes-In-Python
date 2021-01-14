from src import GraphInterface
from src.NodeData import NodeData


class DiGraph:

    def __init__(self):
        self.nodes = {}
        self.edge_size = 0
        self.mc = 0

    def get_node(self, id):
        """return the current node
        """
        if id in self.nodes.keys():
            return self.nodes.get(id)

    def v_size(self):
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
               """
        return len(self.nodes)

    def e_size(self):
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.edge_size

    def get_all_v(self):
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair  (key, node_data)
        """
        return self.nodes

    def all_in_edges_of_node(self, id1: int):
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)
        """
        if not id1 in self.nodes.keys():
            raise ValueError("the node doesn't exist")
        return self.nodes.get(id1).get_neighbors_in()

    def all_out_edges_of_node(self, id1: int):
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,weight)
        """
        if id1 not in self.nodes.keys():
            raise ValueError("the node doesn't exist")
        return self.nodes.get(id1).get_neighbors()

    def get_mc(self):
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float):
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.

        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if not (id1 in self.nodes and id2 in self.nodes) or (weight<=0) or (id1==id2):
            return False
        if id2 not in self.nodes.get(id1).neighbors:
                self.mc += 1
                self.edge_size += 1
                self.nodes.get(id1).add_neighbor(id2,weight)
                self.nodes.get(id2).add_neighbor_in(id1,weight)
                return True
        return False

    def add_node(self, node_id: int, pos: tuple = None):
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.

       Note: if the node id already exists the node will not be added
        """
        if node_id not in self.nodes.keys():
            new_node = NodeData(node_id, pos)
            self.nodes[node_id] = new_node
            self.mc += 1
            return True
        return False

    def remove_node(self, node_id: int):
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        if  node_id in self.nodes.keys():
            for i in self.nodes.keys():
                if node_id in self.nodes[i].get_neighbors():
                    self.mc -= 1
                    self.remove_edge(i, node_id)

            self.edge_size -= len(self.all_out_edges_of_node(node_id))
            self.nodes.pop(node_id)
            self.mc += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int):
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        if node_id1 in self.nodes.keys():
            if node_id2 in self.nodes.get(node_id1).neighbors.keys():
                self.nodes.get(node_id1).remove_neighbor(node_id2)
                self.edge_size -= 1
                self.mc += 1
                return True
        return False

