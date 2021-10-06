'''
  Loop Detection: Given a circular linked list, implement an algorithm that returns
  the node at the beginnning of the loop
'''

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
def display(head: ListNode):
  current = head
  while current:
    print(current.val)
    current = current.next

def isCircular(head: ListNode) -> ListNode:
  if not head: return False 
  slow, fast = head, head.next
  while slow != fast:
    if not fast or not fast.next: 
      return False 
    slow = slow.next 
    fast = fast.next.next
  return True

if __name__ == '__main__':
  from collections import deque
  s = deque() 
  s.append(1)
  s.append(2)
  s.append(3)
  print(s[-1])
  print(s)
  s.pop()
  print(s)
  s.pop() 
  print(s)
  