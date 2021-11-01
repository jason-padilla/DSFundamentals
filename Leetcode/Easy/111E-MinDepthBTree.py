'''
    Given a binary tree, find its minimum depth.
    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
    Note: A leaf is a node with no children. 

    Input: root = [3,9,20,null,null,15,7]
    Output: 2

    Input: root = [2,null,3,null,4,null,5,null,6]
    Output: 5 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left and not root.right:
            return 1
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0: return right + 1 
        elif right == 0: return left + 1
        else:
            return 1 + min(left, right)

#SUMMARY - RECURSION
#0 Go down left and right paths and dont start counting until you reach a node and then start counting on the way up
#1 Our double base case will be if the not root return 0 and if its a node return 1
    #So how would we reach a not root if each check for it on left and right
    #Well when it is a parent node but it only has 1 child it will try to split into left and right again
    #If the left child doesnt exist than it wil reach the base case not root
#2 We want to return 0 on a not node so it doesnt count it and return 1 when we reach a leaf node to increase the count
#3 Then we split into left and right paths 
#4 if the path we returned is 0 than return only the side that isnt 0 and increase by 1 to count that level
#5 When comparing two non 0 paths we want to return the min() and then add 1 to increase the count

            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        if not root.left and not root.right:
            return 1 
        if not root.left and root.right:
            return 1 + self.minDepth(root.right)
        if not root.right and root.left:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))