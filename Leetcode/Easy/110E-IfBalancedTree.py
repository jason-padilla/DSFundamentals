'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
  a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        else:
            return self.helper(root,1)[1]
        
    def helper(self, root, height):
        if not root:
            return (height,True)
        else:
            left, leftBalanced = self.helper(root.left,height+1)
            right, rightBalanced = self.helper(root.right,height+1)
            if abs(left - right) > 1 or leftBalanced == False or rightBalanced == False:
                return (height,False)
            return (max(left,right),True)
#SUMMARY:
#We first want to check if the root exist if it doesnt return True 
#Next if the root does exist than check if both left and right exist
#Now that we have checked for the basics we can move on to the rest of the tree
#The recursive goal is to compare the heights of left and right subtrees
#On every deeper recursive level we increase the height of the tree
#Our recursive base case will be to return (height,True) when the current node is None
#When we compare two left and tree we will return (height,False) 
#If they are equal or witha difference of no more than 1 than we will return (height,True)

#CONDENSED SOLUTION

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node, height)->(int,bool):
            if not node:
                return (height,True)
            else:
                left, leftBalanced = helper(node.left,height+1)
                right, rightBalanced = helper(node.right,height+1)
                if abs(left - right) > 1 or leftBalanced == False or rightBalanced == False:
                    return (height,False)
                return (max(left,right),True)
        return helper(root,1)[1]