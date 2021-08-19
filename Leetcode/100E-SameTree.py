'''
  Given the roots of two binary trees p and q, write a function to check if they are the same or not.

  Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

  Input: p = [1,2,3], q = [1,2,3]
  Output: true

  Input: p = [1,2], q = [1,null,2]
Output: false
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True 
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

#SUMMARY 
#1 Since this is a tree we want to come up with a recursive solution 
#2 First we check to see if p and q are both empty, if they are then theyre equal 
#3 Next check if either is empty if one is empty they are not equal 
#4 Now check if their current values arent equal if they arent then return False 
#5 Since we checked that they are not different we know for sure the current values are equal 
  # We can now move on to the next values 
#6 We recursively make a call comparing the left side of each tree and the right side of the tree 
#7 We 'and' the results to get an either True or False result.

# BIG O 
# Time - O(N) because we only visit each node once
# Space - O(log N) in best case and O(N) in worst 