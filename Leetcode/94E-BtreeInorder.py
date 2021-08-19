'''
  Given the root of a binary tree, return the inorder traversal of its nodes' values.

  #NOTE: Inorder traversal of a B-tree means the order is LNR

  Input: root = [1,null,2,3]
  Output: [1,3,2]
  Example 2:

  Input: root = []
  Output: []
  Example 3:

  Input: root = [1]
  Output: [1]
'''
#SOLUTION 1 RECURSIVE 
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

# SUMMARY 
#1. The basis is simple, we want to add the results from the left+current+right 
#2. If the left is null(None) than we would return an empty [] which will add nothing to our final result 
#3. When a value is available than it will add that value to the list 
#4. Addition of lists is the simplest solution however it is very costful 

#SOLUTION 2 RECURSIVE 
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      return self.dfs(root,result)

    def dfs(self, root, result)-> List[int]:
      if root == None:
        return []
      else:
        result = self.dfs(root.left, result)
        result.append(root.val)
        return self.dfs(root.right, result)
# SUMMARY : dfs because it is a depth first search
#1. With this solution we want to call a helper function that will take in a list as an extra parameter 
#2. The list will start as empty because this will be the result list that will have all of the value nodes
#3. We want to look at the left first and return an empty list when the value is null(None)
#4. Then our current value will be appended to that empty list 
#5. Then we will add all of the right to the left 
#6. Adding all of the right will be the last step and will be the final result

#SOLUTION 3 Iterative
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
# SUMMARY : use a stack
#1. We want to keep track of the current stack and of a results list
#2. We will only add to the result list once the children is None
#3. We want to keep looping as long as root and stack are not empty
#4. We Want to keep going left until the root(current) is not None
#5. If it is None then pop the last value from the stack and add it to the results
#6. We will then make root=root.right but since we are at None than the right root will also be none 
#7. This will prompt the loop to pop the last value from stack again which is technicall the middle node
#8. Then it will add it to the result and move on to the right side  

