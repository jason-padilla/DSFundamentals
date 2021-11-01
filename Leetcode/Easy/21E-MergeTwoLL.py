'''
  Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists. 
  
  Input: l1 = [1,2,4], l2 = [1,3,4]   Input: l1 = [], l2 = []   Input: l1 = [], l2 = [0]
  Output: [1,1,2,3,4,4]               Output: []                Output: [0]
'''
class Solution:
  def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head = res = ListNode(0)
    while l1 or l2:
      if not l1:
        res.next = l2
        l2 = l2.next
      elif not l2:
        res.next = l1
        l1 = l1.next
      else:
        if l1.val <= l2.val:
          res.next = l1
          l1 = l1.next
        else:
          res.next = l2
          l2 = l2.next
      res = res.next
    return head.next

#Cleaner Version
class Solution:
  def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    head = current = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return head.next
        
# SUMMARY
# We need the head node to stay at the head witha dummy node with val 0
# Make the current node equal to the same head node but current is the one thats going to keep moving
# While l1 and l2 are not None keep going, this means that if either one of them becomes None then exit 
# Inside compare l1 and l2, which ever is less is the one that current will point to next
# At the end if either l1 or l2 is None current will point to the rest of the one that isnt None