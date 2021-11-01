'''
  Given the head of a singly linked list, return true if it is a palindrome.
  Input: head = [1,2,2,1]   Input: head = [1,2]
  Output: true              Output: true
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    pal = []
    while head:
      pal.append(head.val)
      head = head.next
    l, r = 0, len(pal)-1
    while l < r:
      if pal[l] != pal[r]:
        return False 
    return True 
#Summary:
# Iterate through the LL and add the values to a list
# Then use two pointers to iterate through the LL and compare the values
# If any of the values don't equal than return False

class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    values = []
    mid, end = head, head 
    while end and end.next:
      values.append(mid.val)
      mid = mid.next 
      end = end.next.next
      if not end:
        mid = mid
      elif not end.next:
        mid = mid.next
    while mid: 
      if mid.val != values.pop():
        return False
      mid = mid.next 
    return True
#Summary 
# Use two pointers to iterate through the LL and half the values to the list and find the mid point
# Then move the mid point to compare the values from the list to all the LL values left 

class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    mid, end = head, head 
    #Find mid point
    while end and end.next:
      mid = mid.next 
      end = end.next.next 
    #Reverse right side of the LL
    prev = None
    while mid:
      temp = mid.next
      mid.next = prev 
      prev = mid
      mid = temp
    #Compare left and right sides
    left, right = head, prev
    while right: 
      if left.val != right.val:
        return False
      left, right = left.next, right.next
    return True
#Summary 
# Use two pointers to find the mid point
# Then reverse the right side 
# Compare the left and right side to see if the LL is a palindrome 