'''
    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
      1
    /   \
  2      2
/   \  /   \
3    4 4    3
Valid
  1
/  \
Valid
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left,root.right)
        
    def helper(self, one:[TreeNode], two:[TreeNode]) -> bool:
        if not one and not two:
            return True
        if not one or not two or  one.val != two.val: 
            return False
        if one.val != two.val:
            return False
        return self.helper(one.left,two.right) and self.helper(one.right, two.left)

#SUMMARY 
#1 When working with trees we will almost always use recursion 
#2 The problem states that we will always be given trees with atleast 1 NOde 
    #so we dont need to check if its None 
#3 What we want to do is split root into two trees and compare those as individual trees 
#4 We do this by calling a helper function that can split it into two 
#5 Then we qcheck if the left is none and right is none 
#6 If not we check if either one is None 
#7 Next we check if there values are not different 
#8 If it passes all of them that means that the values are the same and we should continue comparing 
#9 Will keep comparing until it reaches None for each final Node or the Node Values are not equal