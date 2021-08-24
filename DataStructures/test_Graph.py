import unittest

class Graph: 
  def __init__(self,Nodes=[]):
    self.nodes = Nodes
    self.node_list = {}
    for node in self.nodes: 
      self.node_list[node] = set()

  def __str__(self):
    if not self.node_list: print("{}")
    else:
      for node in self.node_list:
        print(node," -> ",self.node_list[node])

  def display(self):
    if not self.node_list: return "{}"
    else:
      result = ""
      for node in self.node_list:
        result += node + " -> " + str(self.node_list[node])
      return result
  def add_edge(self, a, b):
    if a and b in self.node_list:
      self.node_list[a].add(b)
      self.node_list[b].add(a)

  def add_node(self,node):
    if node not in self.node_list:
      self.node_list[node] = set()

  def del_node(self,node):
    if node in self.node_list:
      for edge in self.node_list[node]:
        self.node_list[edge].remove(node)
      del self.node_list[node]

  def degree(self,node):
    if node in self.node_list:
      return len(self.node_list[node])

class DirectedGraph(Graph): 
  def add_edge(self, a, b):
    if a and b in self.node_list:
      self.node_list[a].add(b)

  def del_node(self,node):
    del self.node_list[node]
    for key in self.node_list:
      if node in self.node_list[key]:
        self.node_list[key].remove(node)

  def get_paths(self, start, end, path=[]):
    path = path+[start]
    if start == end:
      return [path]
    if start not in self.node_list:
      return []
    paths = []
    for city in self.node_list[start]:
      if city not in path:
        new_paths = self.get_paths(city,end,path)
        for p in new_paths: 
          paths.append(p)
    return paths


  def get_shortest_path(self, start, end, path=[]):
    path = path+[start]
    if start == end:
      return path
    if start not in self.node_list:
      return []
    shortest = None
    for city in self.node_list[start]:
      if city not in path:
        new_path = self.get_shortest_path(city,end,path)
        if new_path: 
          if shortest is None or len(shortest) > len(new_path):
            shortest = new_path
    return shortest

class TestLinkedList(unittest.TestCase):
  def test10_empty_graph(self):
    graph = Graph()
    self.assertEqual(graph.display(), "{}")

  def test11_graph_5nodes(self):
    graph = Graph(["A","B","C","D","E"])
    self.assertEqual(graph.display(), "A -> set()B -> set()C -> set()D -> set()E -> set()")
if __name__ == '__main__':
  unittest.main()