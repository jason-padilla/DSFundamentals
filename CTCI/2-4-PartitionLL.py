'''
  Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
  before all nodes gearter than or equal to x. If x is contained within the list, the values of x only need 
  to be after the elements less than x. The partition element x can appear anywhere in the "right partition".
  TLDR: Return a LinkedList where the all values less than target are before all the values greater than target
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

def partition(head: ListNode, target: int) -> ListNode:
  beforeHead = ListNode(0)
  before = beforeHead
  afterHead = ListNode(0)
  after = afterHead 

  while head: 
    if head.val < target:
      before.next = head 
      before = before.next
    else: 
      after.next = head
      after = after.next 
    head = head.next
  after.next = None 
  before.next = afterHead.next 
  return beforeHead.next
#Summary 
#1 Our approach is to have two LinkedList the ones less than target and the ones greater 
#2 At the end we will merge the two linked list and return the merged one
#3 We want to have 4 Nodes two to be runners and two to stay at the head of each linkedlist
#4 We iterate through the head and if the val is less than targ add to before 
#5 We move the runner of before to keep adding to the end of before 
#6 At the end we make after.next = None to cut off any ends 
#7 We make before.next = afterHead.next to merge both LinkedLists and to skip the initial dummy value of afterHead 
#8 Return beforeHead to skip the dummyhead of beforeHead

if __name__ == '__main__':
  alist = ListNode(3)
  alist.next = ListNode(5)
  alist.next.next = ListNode(8)
  alist.next.next.next = ListNode(5)
  alist.next.next.next.next = ListNode(10)
  alist.next.next.next.next.next = ListNode(2)
  alist.next.next.next.next.next.next = ListNode(1)
  partition(alist,5)
  display(alist)