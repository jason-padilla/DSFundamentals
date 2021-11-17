'''
  Given head, the head of a linked list, determine if the linked list has a cycle in it.
  There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
  Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
  Note that pos is not passed as a parameter.
  Return true if there is a cycle in the linked list. Otherwise, return false. 
  Input: head = [3,2,0,-4], pos = 1
  Output: true
  Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
'''
class Solution:
  def hasCycle(self, head: ListNode) -> bool:
    table = {}
    while head:
      try:
        table[head] += 1
        return True
      except:
        table[head] = 1 
      head = head.next
    return False
#Summary 
#1 Put the memory location of each node into a hash table
#2 If the location already exist than that means their is a cycle
 
class Solution:
  def hasCycle(self, head: ListNode) -> bool:
    if not head:
      return False
    slow = head 
    fast = head.next
    while slow != fast:
      if not fast or not fast.next:
        return False
      slow = slow.next
      fast = fast.next.next
    return True

#Summary
#1 This is a fast and slow method, the slow will move at a regular pace
  # the fast will move 2x faster than slow 
#If fast and slow ever equal each other that means their is a cycle