class Graph: 
  def __init__(self,Nodes=[]):
    self.nodes = Nodes
    self.node_list = {}
    for node in self.nodes: 
      self.node_list[node] = set()
      
  def __str__(self):
    if not self.node_list: return "{}"
    else:
      result = ""
      for node in self.node_list:
        result += node + " -> " + str(self.node_list[node]) + "\n"
      return result

  def print(self):
    if not self.nodes: print("{}")
    else:
      print("{")
      for node in self.node_list:
        print(" ",node," -> ",self.node_list[node])
      print("}")
  
  def display(self):
    if not self.node_list: return "{}"
    else:
      result = ""
      for node in self.node_list:
        result += " " + node + " -> " + str(self.node_list[node])
      return result

  def add_edge(self, a, b):
    if a in self.node_list and b in self.node_list:
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
    if a in self.node_list and b in self.node_list:
      self.node_list[a].add(b)

  def del_node(self,node):
    if node in self.node_list:
      del self.node_list[node]
      for key in self.node_list:
        if node in self.node_list[key]:
          self.node_list[key].remove(node)

  def get_paths(self, start, end, path=[]):
    path = path+[start]
    if start == end:
      return [path]
    if start not in self.node_list or end not in self.node_list:
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
    if start not in self.node_list or end not in self.node_list:
      return []
    shortest = None
    for city in self.node_list[start]:
      if city not in path:
        new_path = self.get_shortest_path(city,end,path)
        if new_path: 
          if shortest is None or len(shortest) > len(new_path):
            shortest = new_path
    return shortest
    
if __name__ == "__main__":
  #GRAPH
  all_edges = [("A","B"),("A","C"),("B","D"),("C","D"),("C","E"),("D","E"),("D","E")]
  graph = Graph(["A","B","C","D","E"])
  for edge1,edge2 in all_edges:
    graph.add_edge(edge1, edge2)
  print(graph)

  #DIRECTED GRAPH
  ''' 
            Paris
          /^  |   \ 
    Mumbai    |    ^ New york -> Toronto
          \   |   /^
           ^ Dubai
  '''
  paths = DirectedGraph(["Mumbai","Paris","Dubai","New York","Toronto"])
  routes = [("Mumbai","Paris"),("Mumbai","Dubai"),("Paris","Dubai"),("Paris","New York"),("Dubai","New York"),("New York","Toronto")]
  for fromCity,toCity in routes:
    paths.add_edge(fromCity, toCity)
  print(paths.get_paths("Mumbai","Toronto"))
  print(paths.get_shortest_path("Mumbai","Texas"))
  paths.print()  