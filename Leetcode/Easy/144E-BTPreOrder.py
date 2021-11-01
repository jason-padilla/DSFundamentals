'''
  144 BInary Tree Preorder Traversal
  Given the root of a binary tree, return the preorder traversal of its nodes' values. 
'''
class Solution:
  def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
      return []
    left = self.preorderTraversal(root.left)
    right = self.preorderTraversal(root.right)
    return [root.val] + left + right
#Summary 
#1 If we reach an empty node return an empty list 
#2 Split the root into left and right 
#3 return in the order you want, in this case preorder 

class Solution:
  def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    ret = []
    stack = [root]
    while stack:
      node = stack.pop()
      if node:
        ret.append(node.val)
        stack.append(node.right)
        stack.append(node.left)
    return ret

#Summary 
#1 Put tree into a stack
#2 have an extra list where the results will 
#3 pop the top node which is the 0th item in the stack 
#4 use that node to add the val to results and append the right and left to the stack
#5 appending to the stack will allow us keep adding in preorder because we are adding right and left