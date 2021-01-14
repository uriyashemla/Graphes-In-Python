import unittest
from src.DiGraph import DiGraph
# from src.NodeData import NodeData


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.g = DiGraph()

    def test_v_size(self):
        g = DiGraph()
        self.assertEqual(0, g.v_size())
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        self.assertEqual(3, g.v_size())
        g.remove_node(3)
        self.assertEqual(2, g.v_size())

    def test_e_size(self):
        g = DiGraph()
        self.assertEqual(0, g.e_size())
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1, 2, 3)
        g.add_edge(2, 3, 2)
        g.add_edge(3, 4, 3)
        g.add_edge(4, 1, 2.5)
        self.assertEqual(4, g.e_size())
        g.remove_edge(4, 1)
        self.assertEqual(3, g.e_size())

    def test_all_in_edges_of_node(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1, 2, 3)
        g.add_edge(2, 3, 2)
        g.add_edge(3, 4, 3)
        g.add_edge(4, 1, 2.5)
        self.assertDictEqual({4: 2.5}, g.all_in_edges_of_node(1))
        g.add_edge(2, 1, 0.5)
        self.assertDictEqual({2: 0.5, 4: 2.5}, g.all_in_edges_of_node(1))

    def test_all_out_edges_of_node(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1, 2, 3)
        g.add_edge(2, 3, 2)
        g.add_edge(3, 4, 3)
        g.add_edge(4, 1, 2.5)
        self.assertEqual({2: 3}, g.all_out_edges_of_node(1))
        g.add_edge(1, 4, 1)
        self.assertEqual({2: 3, 4: 1}, g.all_out_edges_of_node(1))

    # def test_get_node(self):
    #     g = DiGraph()
    #     g.add_node(1)
    #     self.assertTrue(g.get_node(1))
    #     # try to get a non exist node
    #     self.assertFalse(g.get_node(2))

    def test_get_mc(self):
        g = DiGraph()
        self.assertEqual(0, g.get_mc())
        g.add_node(1)
        g.add_node(2)
        self.assertEqual(2, g.get_mc())
        g.add_edge(1, 2, 1.5)
        self.assertEqual(3, g.get_mc())
        g.remove_edge(1, 2)
        self.assertEqual(4, g.get_mc())
        g.remove_node(1)
        self.assertEqual(5, g.get_mc())

    def test_add_edge(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        self.assertTrue(g.add_edge(1, 2, 3))
        self.assertTrue(g.add_edge(2, 3, 2))
        self.assertTrue(g.add_edge(3, 4, 3))
        self.assertTrue(g.add_edge(4, 1, 2.5))
        self.assertEqual(4, g.e_size())
        self.assertTrue(g.add_edge(1, 4, 0.5))
        self.assertEqual(5, g.e_size())
        # try to add an edge with non exist nodes
        self.assertFalse(g.add_edge(5, 10, 1.5))
        # try to add an edge with weight < 0
        self.assertFalse(g.add_edge(3, 2, -1))
        # try to add an edge from node to himself
        self.assertFalse(g.add_edge(2, 2, 1))
        # try to add an edge that one of the nodes not exist
        self.assertFalse(g.add_edge(1, 10, 2))
        self.assertEqual(5, g.e_size())

    def test_add_node(self):
        g = DiGraph()
        self.assertEqual(0, g.v_size())
        self.assertTrue(g.add_node(1))
        self.assertTrue(g.add_node(2))
        self.assertEqual(2, g.v_size())
        # try to add a node that already exist
        self.assertFalse(g.add_node(2))
        self.assertEqual(2, g.v_size())

    def test_remove_node(self):
        g = DiGraph()
        self.assertEqual(0, g.v_size())
        self.assertEqual(0, g.e_size())
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1, 2, 3)
        g.add_edge(2, 3, 2)
        g.add_edge(3, 4, 3)
        g.add_edge(4, 1, 2.5)
        self.assertEqual(4, g.v_size())
        self.assertEqual(4, g.e_size())
        self.assertTrue(g.remove_node(1))
        self.assertEqual(3, g.v_size())
        self.assertEqual(2, g.e_size())
        # try to remove non exist node
        self.assertFalse(g.remove_node(1))
        self.assertEqual(3, g.v_size())

    def test_remove_edge(self):
        g = DiGraph()
        self.assertEqual(0, g.e_size())
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1, 2, 3)
        g.add_edge(2, 3, 2)
        g.add_edge(3, 4, 3)
        g.add_edge(4, 1, 2.5)
        self.assertEqual(4, g.e_size())
        self.assertTrue(g.remove_edge(4, 1))
        self.assertEqual(3, g.e_size())
        # try to remove non exist node
        self.assertFalse(g.remove_edge(3, 2))
        # try to remove an edge between non exist nodes
        self.assertFalse(g.remove_edge(5, 10))
        # try to remove an edge while one of the nodes not exist
        self.assertFalse(g.remove_edge(1, 5))
        # try to remove an edge from node to himself
        self.assertFalse(g.remove_edge(3, 3))
        self.assertEqual(3, g.e_size())


if __name__ == '__main__':
    unittest.main()
