'''
  203 REMOVE LINKED LIST ELEMENTS
  Given the head of a linked list and an integer val, 
  remove all the nodes of the linked list that has Node.val == val, and return the new head.

  Example 1:
  Input: head = [1,2,6,3,4,5,6], val = 6
  Output: [1,2,3,4,5]
  
  Example 2:
  Input: head = [], val = 1
  Output: []
  
  Example 3:
  Input: head = [7,7,7,7], val = 7
  Output: []
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:     
    while head:
      if head.val == val:
        head = head.next
      else:
        break
    current = head
    while current and current.next:
      if current.next.val == val:
        current.next = current.next.next
      else:
        current = current.next
    return head

#Summary
#1 We want to remove the head elm if it is equal to the target val
#2 We do this by simply moving the head to the next node 
#3 Next we iterate throught the LL and removing any nodes that equal the target val 

class Solution:
  def removeElements(self, head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    
    dummy_head = ListNode(-1)
    dummy_head.next = head
    head = dummy_head
    current = head
    
    while current.next:
      if current.next.val == val:
        current.next = current.next.next
      else:
          current = current.next
            
    return head.next

#Summary
#1 We create a dummy head node so that if the first node in the linked list is equal to the target
  #we can a prev node to connect it to
#2 Next we iterate throught the LL and removing any nodes that equal the target val 
#3 We return the head.mext because thats what points to the actual head