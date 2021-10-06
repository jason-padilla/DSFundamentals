* LINKED LISTS 
  - A linked list is formed out of nodes 
  - A Node needs to be defined first
  * BIG O  
    - access an element O(n)
    - add/remove at front O(1)
    - add last O(n)
    - add last with tail O(1)
    - add at ith O(n)
  * ADVANTAGES
    1. Use a Lniked List over an array for storing ordered data, if you plan on 
      frequently removing or inserting at the start 
    2. Use a array overa linked list for storing ordered data if you plan on 
      frequently accesing data using an index   
  * PYTHON 
    class Node: 
        def __init__(self,value=None):
          self.value = value 
          self.next = None
    class LinkedList 
      def __init__(self):
        sefl.head = none

* HASH TABLE HASHMAP DICTIONARY 
  - in Python they are called dictionaries
  * BIG O 
    - look up by key O(1)
    - insertion/deletion O(1)
  * SYNTAX 
    - hashTable = {}

    - hashTable = {}

* INORDER TRAVERSAL BINARY TREE 
  * ORDER LNR
    1. Visit Left Child 
    2. Visit Node
    3. Visit Right Child
    - only add a node after you can no longer visit any children 
    - you should add current node before visiting right children 
  * BIG O 
    - N to search 
    - N space or Log N 
  * EXAMPLE
             1
           / | \
         /      \
        2        3
      / | \    / | \
    4      5  6     7
    |      |  |     |
    result = [4,2,5,1,6,3,7]
  * LOOK AT LEETCODE 94
  * RECURSIVE SOLUTION 
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
      def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: 
          return []
        else:
          return [self.inorderTraversal(root.left)] + [root.val] + [self.inorderTraversal(root.right)]
  * ITERATIVE SOLUTION 
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
          stack, result = [], [] 
          while root != None and stack != []:
            while root != None:
              stack.append(root)
              root = root.left 
            root = stack.pop() 
            result.append(root.val)
            root = root.right
          return result

* STACKS 
  * DESC
    - Follows a LIFO operation; Last In First Out 
    - Example use is for browser history: 
      - keeps track of previous links
      - new visited link is added to the top of the stack 
      - can go back to previous link by popping it out 
    - Microsoft Word, Compiler for CTRL+Z 
  * STACKS IN PYTHON LIST VS COLLECTIONS DEQUE 
    - python lists are kind of desgined like stacks 
    - you can .pop() and .push() to a list 
    - however in terms of memory when we add an element thats outside of the 
      amount allocated for the list, the list is duplicated to add more memoery 
    - its better if we use an actual stack like collections.deque 
  * PYTHON COLLECTIONS DEQUE 
    - from collections import deque
    - stack = deque()
    - stack.append("first append") #deque uses append instead of the tradition push
    - stack.append("second append")
    - stack.pop()
    - [1] -> [1,2] -[1,2,3] -> [1,2]
  * BIG O
    - push/pop element : O(1)
    - search elm: O(n)

* QUEUES 
  * DESC 
    - use the form of FIFO; first in first out 
    - same as standing in line, first person that gets there is the first person out 
    - if you think about a list going left->right the next items will always be added to the left so index 0
  * IMPLEMENTATIONS 
    list q = [] q.insert(0,"first") q.insert(0,"second") #-> ['second','first']
    collections.deque q = deque() q.appendleft('first') q.appendleft('second') #-> deque(['second','first'])
  * COLLECTIONS DEQUE AS QUEUE 
    - deque can be used to implement a stack but it can also be used as a queue 
    - q = deque() 
    - q.appendleft(1)
    - q.appendleft(2)
    - q.appendleft(3)
    - q.pop()
    - [1] -> [2,1] -[3,2,1] -> [3,2]
  * BIG O
    - push/pop element : O(1)
    - search elm: O(n)
    
* HEIGHT BALANCED BINARY TREE 
  '''
    Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
    A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
    Explanation: 
      Height Balanced means that each side of a tree or subtree cannot differe by a height of more than 1.
      So we cant have the left side with a height of 2 and the right side with a height of 4>
      This is mainly to prevent a tree from having all of the values on one side which would basically be a linked list not a tree

    [-10,-3,0,5,9]
        0
      /   \
    -10    5
    / \   / \ 
      -3     9
  '''

  #SOLUTION 1
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class Solution:
      def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l,r):
          if l > r: 
            return None 
          m = (l+r)//2
          root = TreeNode(nums[m])
          root.left = helper(l, m-1)
          root.right = helper(m+1,r)
          return root
        return helper(0, len(nums)-1)