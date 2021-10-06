''' 
  Intersection: Given two singly linked lists, determine if the two lists intersect. Return 
  the intersection node. Note that the intersection is defined based on reference, not value. 
  That is, if the kth node of the first linked list is the exact tsame node as the jth node of
  the second linked list, then they are intersecting.
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

def intersect(headA: ListNode, headB: ListNode) -> ListNode:
  '''
    Two pointer swap method, once either point reaches None the one that 
    reaches None will point to the head of the other. If they intersect than
    the loop will end or if they both reach null it will end. 
  '''
  A = headA
  B = headB 
  while A != B: 
    if not A:
      A = headB 
    else:
        A = A.next
    if not B:
      B = headA 
    else:
      B = B.next
  return A

def intersect2(headA: ListNode, headB: ListNode) -> ListNode:
  '''
    Two pointer method but the lens need to be found first and then move the longest one 
    to make it the same len as the shorter one. Then they can move at the same time and 
    compare to see if there is an intersection. 
  '''
  p1, p2 = headA, headB 
  l1, l2 = 0, 0 
  while p1:
    l1 += 1 
    p1 = p1.next 
  while p2:
    l2 += 1 
    p2 = p2.next 
  longer, shorter = headA, headB 
  if l1 < l2: 
    longer, shorter = headB, headA 
  diff = abs(l1 - l2)
  while diff: 
    longer = longer.next
    diff -= 1
  while shorter != longer: 
    shorter = shorter.next 
    longer = longer.next 
  return longer

def intersect3(headA: ListNode, headB: ListNode) -> ListNode:
  ''' 
    Put the references into a hash table and then check if headB equals any
    of the references in the table.
  ''' 
  dix = {}
  while headA:
    dix[headA] = 1
    headA = headA.next 
  while headB: 
    if dix.get(headB):
      return headB 
  return headB

if __name__ == '__main__':
  alist = ListNode(1)
  alist.next = ListNode(2)
  alist.next.next = ListNode(3)
  mid = ListNode(4)
  alist.next.next.next = mid
  alist.next.next.next.next = ListNode(5)
  alist.next.next.next.next.next = ListNode(6)
  alist2 = ListNode(7)
  alist2.next = ListNode(8)
  alist2.next.next = mid
  print(intersect(alist, alist2))