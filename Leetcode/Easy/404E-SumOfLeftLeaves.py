'''
  Given the root of a binary tree, return the sum of all left leaves. 
        3
      /   \
    9       20
  /   \    /   \
          15    7
  Input: root = [3,9,20,null,null,15,7]
  Output: 24
  Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0 
    elif root.left and not root.left.left and not root.left.right:
      return root.left.val + self.sumOfLeftLeaves(root.right)
    else:
      return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) 