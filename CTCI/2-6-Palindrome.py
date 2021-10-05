'''
  Palindrome: Implement a function to check if a linked list is a palindrome.
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

def isPalindrome(head: ListNode) -> bool: 
  mid, end = head, head 
  reversed = []
  while end and end.next:
    reversed.append(mid.val)
    mid = mid.next
    end = end.next.next 
    if not end:
      mid = mid
    elif not end.next:
      mid = mid.next
  front = head
  while mid:
    popped = reversed.pop()
    if popped != mid.val:
      return False 
    mid = mid.next
  return True

if __name__ == '__main__':
  alist = ListNode(1)
  alist.next = ListNode(2)
  alist.next.next = ListNode(3)
  alist.next.next.next = ListNode(4)
  print(isPalindrome(alist))