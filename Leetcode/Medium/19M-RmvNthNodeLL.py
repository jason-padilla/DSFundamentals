'''
  Given the head of a linked list, remove the nth node from the end of the list and return its head. 
  Input: head = [1,2,3,4,5], n = 2
  Output: [1,2,3,5]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    listLen = 0
    curr = runner = head
    while curr:
      listLen += 1
      curr = curr.next
      
    if listLen == 1: return None
    target = listLen - n - 1
    if target < 0: return head.next
    
    while target > 0:
      runner = runner.next
      target -= 1
    runner.next = runner.next.next
    return head