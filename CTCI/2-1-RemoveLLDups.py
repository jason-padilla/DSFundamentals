class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

def removeDups(head: ListNode) -> ListNode:
  unique = set()
  current = head
  unique.add(current.val)
  while current.next:
    if current.next.val in unique:
      current.next = current.next.next
    else:
      unique.add(current.next.val)
      current = current.next 
  return head
#Time: Linear, Space: Linear

def removeDups2(head: ListNode) -> ListNode: 
  unique = set()
  previous = ListNode()
  n = head
  while head: 
    if head.val in unique: 
      previous.next = head.next 
    else:
      unique.add(head.val)
      previous = head 
    head = head.next 
  return n
#Time: Linear, Space: Linear

def removeDupsNoBuffer(head: ListNode):
  current = head 
  while current: 
    runner = current
    while runner.next:
      if runner.next.val == current.val:
        runner.next = runner.next.next
      else:
        runner = runner.next
    current = current.next
#Time: Squared, Space: Constant

def display(head: ListNode):
  current = head
  while current:
    print(current.val)
    current = current.next

if __name__ == '__main__':
  alist = ListNode(1)
  alist.next = ListNode(2)
  alist.next.next = ListNode(3)
  alist.next.next.next = ListNode(1)
  alist.next.next.next.next = ListNode(2)
  alist.next.next.next.next.next = ListNode(3)
  alist.next.next.next.next.next.next = ListNode(3)
  removeDupsNoBuffer((alist))
  display(alist)