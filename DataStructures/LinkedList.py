class Node:
  def __init__(self,val=None):
    self.val = val 
    self.next = None 

class LinkedList: 
  def __init__(self):
    self.head = None
  
  def print(self) -> str:
    if self.head == None: 
      return "None"
    current = self.head 
    result = ""
    while current != None:
      result+= str(current.val) + "->"
      current = current.next 
    result+= "None"
    return result
  
  def push(self,val):
    new_node = Node(val)
    current = self.head 
    new_node.next = current
    self.head = new_node

  def append(self,val):
    if self.head == None: 
      self.head = Node(val)
    else:
      new_node = Node(val)
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node

  def add_at(self,idx, val):
    current = self.head 
    if idx == 0:
      new_node = Node(val)
      new_node.next = current 
      self.head = new_node
    elif current == None: return None 
    else:
      while idx > 1: 
        if current.next == None: 
          return None
        else: 
          idx -= 1 
          current = current.next 
      new_node = Node(val)
      new_node.next = current.next
      current.next = new_node

  def get(self, index):
      current = self.head 
      if current == None: return "Empty Linked List"
      while index > 0:
        if current.next == None:
            return "Out Of Range" 
        index -= 1
        current = current.next 
      return current.val

  def pop(self):
    if self.head == None:
      return "Empty Linked List"
    else:
      current = self.head 
      self.head = current.next 

  def remove_last(self):
    current = self.head 
    if self.head == None: 
      return "Empty Linked List"
    elif current.next == None: 
      self.head = None 
    else:
      while current.next.next != None:
        current = current.next
      current.next = current.next.next 

  def remove_at(self,idx):
    if self.head == None: 
      return None 
    elif idx == 0:
      current = self.head
      self.head = current.next
    else: 
      current = self.head 
      while idx > 1: 
        if current.next.next == None: 
          print("Index out of bounds")
          return
        idx -= 1
        current = current.next 
      current.next = current.next.next 