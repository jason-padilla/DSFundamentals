'''
  You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
  Merge all the linked-lists into one sorted linked-list and return it.
  Input: lists = [[1,4,5],[1,3,4],[2,6]]
  Output: [1,1,2,3,4,4,5,6]
  Explanation: The linked-lists are:
    [ 1->4->5,
      1->3->4,
      2->6 ]
  merging them into one sorted list:
  1->1->2->3->4->4->5->6 
'''

class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    values = []
    for i in lists:
      curr = i 
      while curr:
        values.append(curr.val)
        curr = curr.next
    values.sort()
    head = runner = ListNode(0)
    for i in values:
      runner.next = ListNode(i)
      runner = runner.next
    return head.next