'''
  Sum Lists: You have two numbers represented by a linked list, where each node contains a single 
  digit, The digits are stored in reverse order, such that the 1's digit is at the head of the list.
  Write a function that adds the two numbers and returns the sum as a linked list. 
  Input: (7->1->6) + (5->9->2) => 617 + 295 
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

def sumReturnInt(head1: ListNode, head2: ListNode) -> int:
  ''' 
    Takes in two LinkedLists in reversed order and returns their sum as an integer.
    Input: (7->1->6) + (5->9->2) => 617 + 295 = 912
    Output: 912
  ''' 
  v1 = 0
  v2 = 0
  place = 1
  while head1:
    v1 += head1.val * place 
    place = place * 10
    head1 = head1.next
  place = 1
  while head2:
    v2 += head2.val * place 
    place = place * 10
    head2 = head2.next
  return v1 + v2 

def sumReturnLL(head1: ListNode, head2: ListNode) -> ListNode:
  '''
    Takes two Linked Lists in reversed order and returns a linked list as the sum.
    Input: (7->1->6) + (5->9->2) => 617 + 295 = 912
    Output: (2->1->9) = 912
  '''
  result = ListNode(0)
  resultHead = result
  carry = 0 
  v1 = 0 
  v2 = 0 
  while head1 or head2:
    if head1:
      v1 = head1.val
      head1 = head1.next
    if head2:
      v2 = head2.val
      head2 = head2.next
    result.next = ListNode((v1+v2+carry)%10)
    result = result.next
    carry = (v1+v2) // 10
    v1, v2 = 0, 0
  if carry:
    result.next = ListNode(1)
  return resultHead.next

def sumRecHelper(head1: ListNode, head2: ListNode) -> ListNode:
  if not head1.next and not head2.next: 
    return [ListNode((head1.val + head2.val)% 10) , (head1.val + head2.val) // 10]
  result = sumRecHelper(head1.next, head2.next)
  head, carry = result[0], result[1]
  add = ListNode((head1.val + head2.val + result[1]) % 10)
  add.next = head
  head = add 
  carry = (head1.val + head2.val + carry) // 10
  return [head, carry]

def sumReturnLLInOrder(head1: ListNode, head2: ListNode) -> ListNode:
  '''
    Takes two Linked Lists in order and returns a linked list as the sum.
    Input: (6->1->7) + (2->9->5) => 617 + 295 = 912
    Output: (9->1->2) = 912
  '''
  l1, l2 = 0, 0 
  runner1, runner2 = head1, head2 
  while runner1:
    l1 += 1
    runner1 = runner1.next 
  while runner2:
    l2 += 1
    runner2 = runner2.next
  longer, shorter = None, None
  if l1 > l2: 
    longer, shorter = head1, head2 
  else:
    longer, shorter = head2, head1
    l1, l2 = l2, l1
  zeros = l1 - l2 
  while zeros:
    temp = ListNode(0)
    temp.next = shorter 
    shorter = temp 
    zeros -= 1 
  result = sumRecHelper(longer, shorter)
  result, carry = result[0], result[1]
  if carry: 
    temp = ListNode(1)
    temp.next = result 
    result = temp
  return result 

if __name__ == '__main__':
  alist1 = ListNode(7)
  alist1.next = ListNode(1)
  alist1.next.next = ListNode(6)
  alist2 = ListNode(5)
  alist2.next = ListNode(9)
  alist2.next.next = ListNode(2)
  display(sumReturnLL(alist1, alist2))

  alist1 = ListNode(6)
  alist1.next = ListNode(1)
  alist1.next.next = ListNode(7)
  alist2 = ListNode(2)
  alist2.next = ListNode(9)
  alist2.next.next = ListNode(5)
  display(sumReturnLLInOrder(alist1, alist2))