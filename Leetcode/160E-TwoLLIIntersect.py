'''
  160 Intersection of Two Linked List
  Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
  If the two linked lists have no intersection at all, return null.
  For example, the following two linked lists begin to intersect at node c1: 
  a1 -> a2 \ 
            c1 -> c2 -> c3
  b1 -> b2 /
  return c1

  a1 -> a2 ->
  b1 -> b2 ->
  return None
'''
class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    dix = {}
    if not headA or not headB:
      return None
    while headA:
      try:
        dix[headA] += 1
        return headA
      except:
        dix[headA] = 1
        headA = headA.next 
    while headB:
      try:
        dix[headB] += 1
        return headB
      except:
        dix[headB] = 1
        headB = headB.next
    return None
#Summary
#1 We iterate over all of the nodes from headA and put them in our dictionary 
#2 Then we iterate over headB and see if any of the current nodes are in the dict already 
#3 Runtime is O(n) but space is O(n)

class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    p1 = headA
    p2 = headB
    count1 = 0
    count2 = 0
    while p1:
      p1 = p1.next
      count1 += 1
    while p2:
      p2 = p2.next
      count2 += 1
    if count1 > count2:
      pL = headA
      pS = headB
    else:
      pL = headB
      pS = headA
    diff = abs(count1-count2)
    while diff != 0:
      diff -= 1
      pL = pL.next 
    while pL != pS:
      pL = pL.next
      pS = pS.next
    return pL
#Summary 
#1 Moving catching up method
#2 We first want to figure out the lens of both Linked List 
#3 Then we want to assign which is the longer on and which is the shorter one
#4 We then move the longer one to to be at the same point as the shorter one
#5 We do this by taking the diff of len longer - len shorter and moving longer by such 
#6 Now both longer and shorter will be at the same distance and we can compare to if any of them connect 
#7 we dont need to explicitly return None because if they both reach the end both longer and shorter will be None
  #which will make them equal which will then return None
#8 Runtime: Linear, Space: Constant

class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    p1 = headA
    p2 = headB
    while p1 != p2:
      if p1:
        p1 = p1.next
      else:
        p1 = headB
      if p2:
        p2 = p2.next
      else:
        p2 = headA
    return p1
#Summary 
#1 Swap method 
#2 While p1 and p2 arent equal we continue to move forward 
#3 When p1 reaches its end switch it to the head of B
#4 When p2 reaches its end switch it to the head of A
#5 The trick is that they will be the same len and reach each other at the some point
  # If they have a connecting node they will reach it at the same time and return the node
#6 If they both reach None than they will be equal and return None which means their was no connection
#8 Runtime: Linear, Space: Constant