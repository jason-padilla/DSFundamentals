import unittest
import Graph as mainGraph

class Graph: 
  def __init__(self,Nodes=[]):
    pass

  def __str__(self):
    pass

  def display(self):
    pass

  def add_edge(self, a, b):
    pass

  def add_node(self,node):
    pass

  def del_node(self,node):
    pass

  def degree(self,node):
    pass

class DirectedGraph(Graph): 
  def add_edge(self, a, b):
    pass

  def del_node(self,node):
    pass

  def get_paths(self, start, end, path=[]):
    pass

  def get_shortest_path(self, start, end, path=[]):
    pass

class TestLinkedList(unittest.TestCase):
  def test10_empty_graph(self):
    graph = Graph()
    self.assertEqual(graph.display(), "{}")

  def test11_graph_5nodes(self):
    graph = Graph(["A","B","C","D","E"])
    self.assertEqual(graph.display(), " A -> set() B -> set() C -> set() D -> set() E -> set()")
  
  def test12_add_one_edge(self):
    graph = Graph(["A","B","C","D","E"])
    graph.add_edge("A", "B")
    main = mainGraph.Graph(["A","B","C","D","E"])
    main.add_edge("A", "B")
    self.assertEqual(graph.display(), main.display())

  def test13_add_nonexist_edgeA(self):
    graph = Graph(["A","B","C","D","E"])
    graph.add_edge("F", "B")
    main = mainGraph.Graph(["A","B","C","D","E"])
    main.add_edge("F", "B")
    self.assertEqual(graph.display(), main.display())

  def test14_add_nonexist_edgeB(self):
    graph = Graph(["A","B","C","D","E"])
    graph.add_edge("B", "F")
    main = mainGraph.Graph(["A","B","C","D","E"])
    main.add_edge("B", "F")
    self.assertEqual(graph.display(), main.display())

  def test15_add_nonexist_edgeC(self):
    graph = Graph(["A","B","C","D","E"])
    graph.add_edge("F", "F")
    main = mainGraph.Graph(["A","B","C","D","E"])
    main.add_edge("F", "F")
    self.assertEqual(graph.display(), main.display())

  def test16_add_edges(self):
    all_edges = [("A","B"),("A","C"),("B","D"),("C","D"),("C","E"),("D","E"),("D","E")]
    graph = Graph(["A","B","C","D","E"])
    for edge1,edge2 in all_edges:
      graph.add_edge(edge1, edge2)
    main = mainGraph.Graph(["A","B","C","D","E"])
    for edge1,edge2 in all_edges:
      main.add_edge(edge1, edge2)
    self.assertEqual(graph.display(),main.display())
  
  def test17_add_new_node(self):
    graph = Graph(["A","B","C","D","E"])
    graph.add_node("F")
    main = mainGraph.Graph(["A","B","C","D","E"])
    main.add_node("F")
    self.assertEqual(graph.display(),main.display())

  def test18_add_existing_node(self):
    graph = Graph(["A","B","C","D","E"])
    graph.add_node("A")
    main = mainGraph.Graph(["A","B","C","D","E"])
    main.add_node("A")
    self.assertEqual(graph.display(),main.display())

  def test17_del_node(self):
    graph = Graph(["A","B","C","D","E"])
    graph.del_node("A")
    main = mainGraph.Graph(["A","B","C","D","E"])
    main.del_node("A")
    self.assertEqual(graph.display(),main.display())

  def test18_del_nonexisting_node(self):
    graph = Graph(["A","B","C","D","E"])
    graph.del_node("F")
    main = mainGraph.Graph(["A","B","C","D","E"])
    main.del_node("F")
    self.assertEqual(graph.display(),main.display())

  def test19_node_degree(self):
    graph = Graph(["A","B","C","D","E"])
    graph.degree("A")
    main = mainGraph.Graph(["A","B","C","D","E"])
    main.degree("A")
    self.assertEqual(graph.display(),main.display())
  
  def test20_nonexisting_node_degree(self):
    graph = Graph(["A","B","C","D","E"])
    graph.degree("F")
    main = mainGraph.Graph(["A","B","C","D","E"])
    main.degree("F")
    self.assertEqual(graph.display(),main.display())

  def test21_DG_empty(self):
    Dgraph = DirectedGraph()
    main = mainGraph.DirectedGraph()
    self.assertEqual(Dgraph.display(),main.display())

  def test22_DG_(self):
    Dgraph = DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    main = mainGraph.DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    self.assertEqual(Dgraph.display(),main.display())

  def test23_DG_add_edge(self):
    Dgraph = DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    Dgraph.add_edge("Mumbai", "Toronto")
    main = mainGraph.DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    main.add_edge("Mumbai", "Toronto")
    self.assertEqual(Dgraph.display(),main.display())

  def test24_DG_add_nonexisting_edgeA(self):
    Dgraph = DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    Dgraph.add_edge("Mumbai", "Texas")
    main = mainGraph.DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    main.add_edge("Mumbai", "Texas")
    self.assertEqual(Dgraph.display(),main.display())

  def test25_DG_add_nonexisting_edgeB(self):
    Dgraph = DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    Dgraph.add_edge("Texas", "Mumbai")
    main = mainGraph.DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    main.add_edge("Texas", "Mumbai")
    self.assertEqual(Dgraph.display(),main.display())

  def test26_DG_add_nonexisting_edgeC(self):
    Dgraph = DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    Dgraph.add_edge("Texas", "Texas")
    main = mainGraph.DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    main.add_edge("Texas", "Texas")
    self.assertEqual(Dgraph.display(),main.display())

  def test27_DG_del_node(self):
    Dgraph = DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    Dgraph.del_node("Mumbai")
    main = mainGraph.DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    main.del_node("Mumbai")
    self.assertEqual(Dgraph.display(),main.display())

  def test28_DG_del_nonexisting_node(self):
    Dgraph = DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    Dgraph.del_node("Texas")
    main = mainGraph.DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    main.del_node("Texas")
    self.assertEqual(Dgraph.display(),main.display())

  def test29_DG_get_paths(self):
    Dgraph = DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      Dgraph.add_edge(fromCity, toCity)
    Dgraph.get_paths("Mumbai", "New York")
    main = mainGraph.DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      main.add_edge(fromCity, toCity)
    main.get_paths("Mumbai", "New York")
    self.assertEqual(Dgraph.display(),main.display())

  def test30_DG_get_paths_to_self(self):
    Dgraph = DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      Dgraph.add_edge(fromCity, toCity)
    Dgraph.get_paths("Mumbai", "Mumbai")
    main = mainGraph.DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      main.add_edge(fromCity, toCity)
    main.get_paths("Mumbai", "Mumbai")
    self.assertEqual(Dgraph.display(),main.display())

  def test31_DG_get_paths_to_nonexisting(self):
    Dgraph = DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      Dgraph.add_edge(fromCity, toCity)
    Dgraph.get_paths("Mumbai", "Texas")
    main = mainGraph.DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      main.add_edge(fromCity, toCity)
    main.get_paths("Mumbai", "Texas")
    self.assertEqual(Dgraph.display(),main.display())

  def test32_DG_get_paths_from_nonexisting(self):
    Dgraph = DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      Dgraph.add_edge(fromCity, toCity)
    Dgraph.get_paths("Texas", "Mumbai")
    main = mainGraph.DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      main.add_edge(fromCity, toCity)
    main.get_paths("Texas", "Mumbai")
    self.assertEqual(Dgraph.display(),main.display())
  
  def test33_DG_get_paths_tofrom_nonexisting(self):
    Dgraph = DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      Dgraph.add_edge(fromCity, toCity)
    Dgraph.get_paths("Texas", "Texas")
    main = mainGraph.DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      main.add_edge(fromCity, toCity)
    main.get_paths("Texas", "Texas")
    self.assertEqual(Dgraph.display(),main.display())

  def test34_DG_getshortest_paths(self):
    Dgraph = DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      Dgraph.add_edge(fromCity, toCity)
    Dgraph.get_shortest_path("Mumbai", "New York")
    main = mainGraph.DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      main.add_edge(fromCity, toCity)
    main.get_shortest_path("Mumbai", "New York")
    self.assertEqual(Dgraph.display(),main.display())

  def test35_DG_getshortest_paths_to_self(self):
    Dgraph = DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      Dgraph.add_edge(fromCity, toCity)
    Dgraph.get_shortest_path("Mumbai", "Mumbai")
    main = mainGraph.DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      main.add_edge(fromCity, toCity)
    main.get_shortest_path("Mumbai", "Mumbai")
    self.assertEqual(Dgraph.display(),main.display())

  def test36_DG_getshortest_paths_to_nonexisting(self):
    Dgraph = DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      Dgraph.add_edge(fromCity, toCity)
    Dgraph.get_shortest_path("Mumbai", "Texas")
    main = mainGraph.DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      main.add_edge(fromCity, toCity)
    main.get_shortest_path("Mumbai", "Texas")
    self.assertEqual(Dgraph.display(),main.display())

  def test37_DG_getshortest_paths_from_nonexisting(self):
    Dgraph = DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      Dgraph.add_edge(fromCity, toCity)
    Dgraph.get_shortest_path("Texas", "Mumbai")
    main = mainGraph.DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      main.add_edge(fromCity, toCity)
    main.get_shortest_path("Texas", "Mumbai")
    self.assertEqual(Dgraph.display(),main.display())
  
  def test38_DG_getshortest_paths_tofrom_nonexisting(self):
    Dgraph = DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      Dgraph.add_edge(fromCity, toCity)
    Dgraph.get_shortest_path("Texas", "Texas")
    main = mainGraph.DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
    routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
    for fromCity,toCity in routes:
      main.add_edge(fromCity, toCity)
    main.get_shortest_path("Texas", "Texas")
    self.assertEqual(Dgraph.display(),main.display())

if __name__ == '__main__':
  unittest.main()