class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
def display(head: ListNode):
  current = head
  while current:
    print(current.val)
    current = current.next

def delMid(head: ListNode):
  if not head or not head.next:
    head = None
  elif not head.next.next:
    head.next = None
  else:
    prev = None
    p1 = head 
    p2 = head
    while p2.next and p2.next.next:
      prev = p1
      p1 = p1.next 
      p2 = p2.next.next
    prev.next = p1.next 
#Summary 
#1 Two pointer method 
#2 One pointer moves normally and the other moves twice as fast 
#3 by the time p2 reaches end, p1 will be at mid
#4 Prev points to the pointer before p1, so to remove mid we just need to connect prev.next = p1.next 

if __name__ == '__main__':
  alist = ListNode(1)
  alist.next = ListNode(2)
  alist.next.next = ListNode(3)
  alist.next.next.next = ListNode(4)
  alist.next.next.next.next = ListNode(5)
  alist.next.next.next.next.next = ListNode(6)
  alist.next.next.next.next.next.next = ListNode(7)
  delMid(alist)
  display(alist)