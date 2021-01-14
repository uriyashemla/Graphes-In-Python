import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.NodeData import NodeData


class MyTestCase(unittest.TestCase):

    def test_get_graph(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1, 2, 3)
        g.add_edge(2, 3, 2)
        g.add_edge(3, 4, 3)
        g.add_edge(4, 1, 2.5)
        ga = GraphAlgo(g)
        self.assertEqual(g, ga.get_graph())

    def test_save_and_load(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1, 2, 3)
        g.add_edge(2, 3, 2)
        g.add_edge(3, 4, 3)
        g.add_edge(4, 1, 2.5)
        ga = GraphAlgo(g)
        self.assertTrue(ga.save_to_json("../graph.txt"))
        self.assertTrue(ga.load_from_json("../graph.txt"))

    def test_shortest_path(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1, 2, 3)
        g.add_edge(2, 3, 2)
        g.add_edge(3, 4, 3)
        g.add_edge(4, 1, 2.5)
        ga = GraphAlgo(g)
        self.assertEqual((5.0, [1, 2, 3]), ga.shortest_path(1, 3))
        ga.get_graph().remove_edge(2, 3)
        # try to find the shortest path between 2 nodes that not connected
        self.assertTupleEqual((float('inf'), []), ga.shortest_path(1, 3))
        # try to find the shortest path while one of the nodes not exist
        self.assertListEqual([], ga.shortest_path(1, 5))
        # try to find the shortest path with non exist nodes
        self.assertListEqual([], ga.shortest_path(5, 10))
        # try to find the shortest path from node to himself
        self.assertTupleEqual((0, [1]), ga.shortest_path(1, 1))
        # try to find the shortest path from non exist node to himself
        self.assertListEqual([], ga.shortest_path(5, 5))

    def test_connected_component(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        self.assertListEqual([], ga.connected_component(1))
        ga.get_graph().add_node(1)
        ga.get_graph().add_node(2)
        ga.get_graph().add_node(3)
        ga.get_graph().add_node(4)
        ga.get_graph().add_node(5)
        ga.get_graph().add_node(6)
        ga.get_graph().add_node(7)
        ga.get_graph().add_node(8)
        ga.get_graph().add_edge(1, 2, 1)
        ga.get_graph().add_edge(3, 1, 2)
        ga.get_graph().add_edge(2, 3, 3)
        ga.get_graph().add_edge(2, 4, 2.5)
        ga.get_graph().add_edge(4, 1, 4)
        ga.get_graph().add_edge(5, 8, 1)
        ga.get_graph().add_edge(7, 6, 2)
        ga.get_graph().add_edge(6, 5, 3)
        ga.get_graph().add_edge(8, 6, 4)
        self.assertListEqual([1, 2, 3, 4], ga.connected_component(1))
        self.assertListEqual([8, 5, 6], ga.connected_component(5))
        self.assertListEqual([7], ga.connected_component(7))
        ga.get_graph().add_node(10)
        self.assertListEqual([10], ga.connected_component(10))
        # try to find the SCC of unknown node
        self.assertListEqual([], ga.connected_component(0))

    def test_connected_components(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        self.assertListEqual([], ga.connected_component(1))
        ga.get_graph().add_node(1)
        ga.get_graph().add_node(2)
        ga.get_graph().add_node(3)
        ga.get_graph().add_node(4)
        ga.get_graph().add_node(5)
        ga.get_graph().add_node(6)
        ga.get_graph().add_node(7)
        ga.get_graph().add_node(8)
        ga.get_graph().add_edge(1, 2, 1)
        ga.get_graph().add_edge(3, 1, 2)
        ga.get_graph().add_edge(2, 3, 3)
        ga.get_graph().add_edge(2, 4, 2.5)
        ga.get_graph().add_edge(4, 1, 4)
        ga.get_graph().add_edge(5, 8, 1)
        ga.get_graph().add_edge(7, 6, 2)
        ga.get_graph().add_edge(6, 5, 3)
        ga.get_graph().add_edge(8, 6, 4)
        self.assertListEqual([[1, 2, 3, 4], [8, 5, 6], [7]], ga.connected_components())


if __name__ == '__main__':
    unittest.main()
