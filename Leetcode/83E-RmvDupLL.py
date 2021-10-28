'''
  Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
  1->1->2->3->3 = 1->2->3
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    if curr:
      while curr.next:
        if curr.val == curr.next.val:
          curr.next = curr.next.next
        else:
          curr = curr.next
      return head