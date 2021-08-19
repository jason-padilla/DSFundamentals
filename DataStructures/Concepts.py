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