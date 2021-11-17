'''
105 REVERSE LINKED LIST
  Given the head of a singly linked list, reverse the list, and return the reversed list.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head: return head
    current = head.next
    rev_head = ListNode(head.val)
    while current:
      temp = ListNode(current.val)
      temp.next = rev_head
      rev_head = temp
      current = current.next
    return rev_head
#Summary 
#1 Reverse a linked list by adding the values to the head of a new linked list
#2 Time: Linear, Space: Linear

class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head
    while current:
      temp = current.next 
      current.next = prev 
      prev = current 
      current = temp
    return prev
#Summary 
#1 Reverse a LL by first setting the next value into a temp val 
#2 Then make the next value point a to the prev value 
#3 Change prev to now be current; this essentialy moves the pointer of prev
#4 Finally move current to temp which points to the orginal next value 
#5 Time: Linear, Space: Constant