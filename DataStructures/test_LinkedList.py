import unittest

class Node:
  def __init__(self,val=None):
    pass
class LinkedList: 
  def __init__(self):
    pass
  
  def print(self) -> str:
    pass
  
  def push(self,val):
    pass

  def append(self,val):
    pass

  def add_at(self,idx, val):
    
    pass

  def get(self, index):
    pass

  def pop(self):
    pass

  def remove_last(self):
    pass

  def remove_at(self,idx):
    pass

class TestLinkedList(unittest.TestCase):
  def test1_empty(self):
    L1 = LinkedList()
    self.assertEqual("None", L1.print())

  def test2_push_empty(self):
    L1 = LinkedList()
    L1.push(0)
    self.assertEqual(L1.print(), "0->None")

  def test3_push_3(self):
    L1 = LinkedList()
    L1.push(0)
    L1.push(1)
    L1.push(2)
    self.assertEqual(L1.print(), "2->1->0->None")

  def test4_append_empty(self):
    L1 = LinkedList()
    L1.append(0)
    self.assertEqual(L1.print(), "0->None")

  def test5_append_full(self):
    L1 = LinkedList()
    L1.push(1)
    L1.push(2)
    L1.push(3)
    L1.append(0)
    self.assertEqual(L1.print(), "3->2->1->0->None")

  def test6_add_at_empty(self):
    L1 = LinkedList()
    L1.add_at(1,0)
    self.assertEqual(L1.print(), "None")

  def test7_add_at_zero_empty(self):
    L1 = LinkedList()
    L1.add_at(0,0)
    self.assertEqual(L1.print(), "0->None")  

  def test8_add_at_zero(self):
    L1 = LinkedList()
    L1.push(0)
    L1.add_at(0,1)
    self.assertEqual(L1.print(), "1->0->None")  

  def test90_add_at_middle(self):
    L1 = LinkedList()
    L1.push(1)
    L1.push(2)
    L1.push(4)
    L1.push(5)
    L1.add_at(2,3)
    self.assertEqual(L1.print(), "5->4->3->2->1->None")  

  def test91_add_at_end(self):
    L1 = LinkedList()
    L1.push(1)
    L1.push(2)
    L1.push(3)
    L1.push(4)
    L1.add_at(4,0)
    self.assertEqual(L1.print(), "4->3->2->1->0->None") 

  def test92_add_at_outofrange(self):
    L1 = LinkedList()
    L1.push(0)
    L1.push(1)
    L1.push(2)
    L1.add_at(5,0)
    self.assertEqual(L1.print(), "2->1->0->None")  

  def test93_get_empty(self):
    L1 = LinkedList()
    self.assertEqual(L1.get(2), "Empty Linked List")

  def test94_get_front(self):
    L1 = LinkedList()
    L1.push(1)
    L1.push(2)
    L1.push(3)
    self.assertEqual(L1.get(0), 3)

  def test95_get_back(self):
    L1 = LinkedList()
    L1.push(1)
    L1.push(2)
    L1.push(3)
    self.assertEqual(L1.get(2), 1)  

  def test96_get_middle(self):
    L1 = LinkedList()
    L1.push(1)
    L1.push(2)
    L1.push(3)
    self.assertEqual(L1.get(1), 2)  

  def test98_get_outofrange(self):
    L1 = LinkedList()
    L1.push(1)
    L1.push(2)
    L1.push(3)
    self.assertEqual(L1.get(5), "Out Of Range")  

  def test_pop_empty(self):
    L1 = LinkedList()
    self.assertEqual(L1.get(5), "Empty Linked List")  

  def test_pop_1(self):
    L1 = LinkedList()
    L1.push(1)
    L1.pop()
    self.assertEqual(L1.print(), "None")

  def test_pop_3(self):
    L1 = LinkedList()
    L1.push(1)
    L1.push(2)
    L1.push(3)
    L1.pop()
    self.assertEqual(L1.print(), "2->1->None")  

  def test_remove_last(self):
    L1 = LinkedList()
    L1.remove_last()
    self.assertEqual(L1.print(), "None")

  def test_remove_last_one(self):
    L1 = LinkedList()
    L1.push(1)
    L1.remove_last()
    self.assertEqual(L1.print(), "None")

  def test_remove_last_full(self):
    L1 = LinkedList()
    L1.push(1)
    L1.push(2)
    L1.push(3)
    L1.remove_last()
    self.assertEqual(L1.print(), "3->2->None")  
  
  def test_remove_at(self):
    L1 = LinkedList()
    L1.remove_at(1)
    self.assertEqual(L1.print(), "None")

  def test_remove_at_zero(self):
    L1 = LinkedList()
    L1.push(1)
    L1.remove_at(0)
    self.assertEqual(L1.print(), "None")

  def test_remove_at_front(self):
    L1 = LinkedList()
    L1.push(1)
    L1.push(2)
    L1.push(3)
    L1.remove_at(0)
    self.assertEqual(L1.print(), "2->1->None")

  def test_remove_at_middle(self):
    L1 = LinkedList()
    L1.push(1)
    L1.push(2)
    L1.push(3)
    L1.remove_at(1)
    self.assertEqual(L1.print(), "3->1->None")

  def test_remove_at_end(self):
    L1 = LinkedList()
    L1.push(1)
    L1.push(2)
    L1.push(3)
    L1.remove_at(2)
    self.assertEqual(L1.print(), "3->2->None")

  def test_remove_at_outofrange(self):
    L1 = LinkedList()
    L1.push(1)
    L1.push(2)
    L1.push(3)
    L1.remove_at(5)
    self.assertEqual(L1.print(), "3->2->1->None")

if __name__ == '__main__':
  unittest.main()

# class Node:
#   def __init__(self,val=None):
#     pass
# class LinkedList: 
#   def __init__(self):
#     pass
  
#   def print(self) -> str:
#     pass
  
#   def push(self,val):
#     pass

#   def append(self,val):
#     pass

#   def add_at(self,idx, val):
    
#     pass

#   def get(self, index):
#     pass

#   def pop(self):
#     pass

#   def remove_last(self):
#     pass

#   def remove_at(self,idx):
#     pass