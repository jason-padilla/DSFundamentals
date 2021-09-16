'''
  Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that 
  adding up all the values along the path equals targetSum. A leaf is a node with no children. 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        diff = targetSum-root.val
        if not root.left and not root.right:
            return diff == 0
        left = self.hasPathSum(root.left, diff)
        right = self.hasPathSum(root.right, diff)
        return left or right

#Summary 
#1 As always with a tree we want to use recursion 
#2 What we want to do is subtract the current value from the current Target 
  # If the difference btwn the two is 0 and the current node is a leaf node than we return True 
#3 If the difference isnt 0 than we keep going down the path left and right 
#4 Our base case will be that when we reach an empty node we return False
  # We return False because this would mean that 1 level higher we didnt get a diff of 0 
#5 going up through the recursion we compare left and right by doing (left or right)
  #Using the OR comparison will return True if any of the paths added to targetSum