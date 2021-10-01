'''
  Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list
'''

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def findKth(head: ListNode, k: int ) -> int:
  current = head
  size = 0
  while current:
    size += 1
    current = current.next 
  target = size - k
  runner = head
  while target > 0:
    target -= 1
    runner = runner.next 
  return runner.val
#Summary 
#1 We find the len of the linked list by iterating through it and keeping a count 
#2 To find the kth to last value we subtract size - k 
#3 Then we subtract from the count until we reach the kth to last value 

def findKthPointers(head: ListNode, k: int ) -> int:
  p1 = head 
  p2 = head 
  for i in range(k):
    p1 = p1.next 
  while p1:
    p1 = p1.next 
    p2 = p2.next 
  return p2.val 
#Summary 
#1 Two pointer method we move p1 by kth amount
#2 Then we move both p1 and p2 at the same time, when p1 reaches the end p2 will be at kth

def findKthRecursive(head: ListNode, k: int ) -> int:
  if head == None:
    return 0
  idx = findKthRecursive(head.next, k) + 1
  if idx == k:
    return head.val
    print("Found kth value:", head.val)
  return idx 
#Summary 
#1 Not as efficient and doesnt return the value, it only outputs it 
#2 We recursively go down till we rach None and then go back up counting
#3 If the count equals kth than we output the value which will exit us out of the function 
if __name__ == '__main__':
  alist = ListNode(1)
  alist.next = ListNode(2)
  alist.next.next = ListNode(3)
  alist.next.next.next = ListNode(4)
  alist.next.next.next.next = ListNode(5)
  alist.next.next.next.next.next = ListNode(6)
  alist.next.next.next.next.next.next = ListNode(7)
  # print(findKth(alist, 0))
  # print(findKthPointers(alist, 7))
  # findKthRecursive(alist, 3)