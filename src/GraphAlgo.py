from queue import Queue
from queue import LifoQueue
from queue import PriorityQueue
from src.DiGraph import DiGraph
import json
import matplotlib.pyplot as plt
import numpy as np
import random


class GraphAlgo:

    def __init__(self, graph=None):
        if graph is not None:
            self.graph = graph
        else:
            self.graph = DiGraph()

    def get_graph(self):
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.graph

    def load_from_json(self, file_name: str):
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        try:
            with open(file_name, "r") as file:
                my_dict = json.load(file)
                edges_list = my_dict["Edges"]
                nodes_list = my_dict["Nodes"]
                graph = DiGraph()
                for n in nodes_list:
                    if "pos" in n:
                        max_split = 2
                        pos = [float(i) for i in n["pos"].split(",", max_split)]
                        graph.add_node(n["id"], (pos[0], pos[1], pos[2]))
                    else:
                        graph.add_node(n["id"])
                for e in edges_list:
                    graph.add_edge(e["src"], e["dest"], e["w"])
                    self.graph = graph
                return True
        except IOError as e:
            print(e)
            return False
        finally:
            file.close()

    def save_to_json(self, file_name: str):
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        if self.graph is None:
            return False

        my_dict = {"Nodes": [], "Edges": []}
        try:
            with open(file_name, "w") as file:
                for v in self.get_graph().get_all_v().values():
                    n = self.get_graph().get_node(v.get_key())
                    if n.get_pos() is None:
                        id_node = v.get_key()
                        v_dict = {"id": id_node}
                        my_dict["Nodes"].append(v_dict)
                    else:
                        pos = str(v.get_pos().get_x()) + "," + str(v.get_pos().get_y()) + "," + str(v.get_pos().get_z)
                        id_node = v.get_key()
                        v_dict = {"pos": pos, "id": id_node}
                        my_dict["Nodes"].append(v_dict)
                for node in self.graph.get_all_v().values():
                    for ni in node.get_neighbors().keys():
                        my_dict["Edges"].append({"src": node.get_key(), "dest": self.graph.get_node(ni).get_key(), "w" : node.get_neighbors().get(ni)})

                json.dump(my_dict,default=lambda m:m.__dict__,indent=4, fp=file)
                return True
        except IOError as e:
            print(e)
            return False
        finally:
            file.close()

    def shortest_path(self, id1: int, id2: int):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list
        """
        if id1 not in self.graph.get_all_v().keys() or id2 not in self.graph.get_all_v().keys():
            return []
        path = []
        if id1 == id2:
            path.append(self.graph.get_node(id1).get_key())
            return (0, path)
        # set for each node its own weight from the src node by BFS algorithm
        queue = PriorityQueue()
        self.graph.get_node(id1).set_weight(0)
        queue.put(self.graph.get_node(id1))
        while not queue.empty():
            cur_node = queue.get()
            if cur_node.get_key() == id2:
                break
            if cur_node.get_info() != "Black":
                w = cur_node.get_weight()
                for n in self.graph.all_out_edges_of_node(cur_node.get_key()).keys():
                    nodi = self.graph.get_node(n)
                    if nodi.get_weight() > w + self.graph.get_node(cur_node.get_key()).get_neighbors().get(nodi.get_key()) or nodi.get_weight() == -1:
                        nodi.set_weight(w + self.graph.get_node(cur_node.get_key()).get_neighbors().get(nodi.get_key()))
                    if nodi.get_info() == "White":
                        queue.put(nodi)
                        nodi.set_info("Grey")
            cur_node.set_info("Black")
        # if theres no connection, sets all the nodes to the original initialize and return (float('inf'), path)
        the_shortest_path = self.graph.get_node(id2).get_weight()
        if the_shortest_path == -1:
            for n in self.graph.get_all_v().keys():
                removing = self.graph.get_node(n)
                removing.set_info("White")
                removing.set_weight(-1)
            return (float('inf'), path)

        # creating a copied graph with the same nodes and edges but they are going backwards (the edges are turn to the opposite direction)
        the_new_graph = DiGraph()
        for n in self.graph.get_all_v():
            the_new_graph.add_node(n)
            the_new_graph.get_node(n).set_weight(self.graph.get_node(n).get_weight())
        for n in self.graph.get_all_v():
            nodia = self.graph.get_node(n)
            for nei in self.graph.all_out_edges_of_node(nodia.get_key()).keys():
                nodiab = self.graph.get_node(nei)
                the_new_graph.add_edge(nodiab.get_key(),nodia.get_key(),self.graph.all_out_edges_of_node(nodia.get_key()).get(nodiab.get_key()))
        des = the_new_graph.get_node(id2)

        # creating a stack and adding it the nodes that are leading from the src node to the dest node
        # and checking if the current node is the correct one that lead from the src node
        stack = LifoQueue()
        while True:
            if des.get_weight() == 0:
                stack.put(des)
                break
            for n in the_new_graph.all_out_edges_of_node(des.get_key()):
                nod = the_new_graph.get_node(n)
                if des.get_weight() == nod.get_weight() + the_new_graph.all_out_edges_of_node(des.get_key()).get(nod.get_key()):
                    stack.put(des)
                    des=nod
                    break
        while not stack.empty():
            path.append(stack.get().get_key())

        # sets all the nodes to the original initialize
        for n in self.graph.get_all_v().keys():
            no = self.graph.get_node(n)
            no.set_info("White")
            no.set_weight(-1)

        return (the_shortest_path,path)

    def connected_component(self, id1: int):
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        if id1 not in self.graph.get_all_v().keys():
            return []
        list1 = [id1]
        list2 = [id1]
        queue = Queue()
        queue.put(id1)
        while not queue.empty():
            curr = queue.get()
            for i in self.graph.all_out_edges_of_node(curr).keys():
                if self.graph.nodes[i].get_info() != "Black":
                    list1.append(i)
                    queue.put(i)
            self.graph.nodes[curr].set_info("Black")
        queue.put(id1)
        while not queue.empty():
            curr = queue.get()
            for i in self.graph.all_in_edges_of_node(curr).keys():
                if self.graph.nodes[i].get_tag() != 0:
                    list2.append(i)
                    queue.put(i)
            self.graph.get_node(curr).set_tag(0)
        for n in self.graph.get_all_v().keys():
            self.graph.nodes[n].set_tag(-1)
            self.graph.nodes[n].set_info("White")

        the_list = list(set(list1).intersection(list2))
        return the_list
    def connected_components(self):
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        list = []
        flag = True
        nodes = set(self.graph.get_all_v().keys())
        while flag:
            list1 = self.connected_component(nodes.pop())
            list.append(list1)
            nodes = set(nodes)-set(list1)
            if len(nodes) == 0:
                flag = False
        return list

    def plot_graph(self):
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        x = []
        y = []

        for n in self.graph.get_all_v().values():
            if(n.get_pos() != None):
                x.append(n.get_pos().get_x())
                y.append(n.get_pos().get_y())
            else:
                x_random = random.random()
                y_random = random.random()
                n.set_pos(x_random, y_random, 0)
                x.append(x_random)
                y.append(y_random)
        fig, ax = plt.subplots()
        ax.scatter(x, y, 60, "red")
        for xi in self.graph.get_all_v().values():
            for yi in self.graph.all_out_edges_of_node(xi.get_key()):
                src = (xi.get_pos().get_x(), xi.get_pos().get_y())
                dest = (self.graph.get_node(yi).get_pos().get_x(), self.graph.get_node(yi).get_pos().get_y())
                plt.annotate("", dest, src, arrowprops=dict(edgecolor="black", arrowstyle="->"))

        plt.title("OOP - Ex3")
        plt.xlabel("x axis")
        plt.ylabel("y axis")
        plt.show()
