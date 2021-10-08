'''
  235 Lowest Common Ancestor of a Binary Search Tree
  Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
  According to the definition of LCA on Wikipedia: 
  “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
  (where we allow a node to be a descendant of itself).”
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if p.val > root.val and q.val > root.val:
      return self.lowestCommonAncestor(root.right, p, q)
    elif p.val < root.val and q.val < root.val:
      return self.lowestCommonAncestor(root.left, p, q)
    else:
      return root 
#Summary 
# The LCA will be the value that is in between p and q
# If both values are bigger than move right
# If both values are lower than move left

class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    while root:
      if p.val > root.val and q.val > root.val:
        root = root.right
      elif p.val < root.val and q.val < root.val:
        root = root.left
      else:
        return root 