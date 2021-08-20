'''
  Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
  A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
  Explanation: 
    Height Balanced means that each side of a tree or subtree cannot differe by a height of more than 1.
    So we cant have the left side with a height of 2 and the right side with a height of 4>
    This is mainly to prevent a tree from having all of the values on one side which would basically be a linked list not a tree

  [-10,-3,0,5,9]
      0
    /   \
  -10    5
  / \   / \ 
    -3     9
'''

#SOLUTION 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
      def helper(l,r):
        if l > r: 
          return None 
        m = (l+r)//2
        root = TreeNode(nums[m])
        root.left = helper(l, m-1)
        root.right = helper(m+1,r)
        return root
      return helper(0, len(nums)-1)
#SUMMARY 
#1 So the way we want to approach this problem is to have 3 pointers a Left Middle Right 
#2 The middle point is what will be the root for each tree/subtree and the Left/Right will be the recursive branches 
#3 We get the first middle by doing (L+R)//2 so 0,Len(nums)//2; the first index and the farthest index 
#4 We then assign the middle to be the root 
#5 After, we diverge into smaller trees the left tree will be Left->1 before Middle 
  #Right tree will be 1 after Middle->Right 
#6 The base statement will be when Left value becomes bigger than Right value 
  #This is a standard rule when doing binary search, 
    # Left Tree: Left will stay the same and Right will be decreasing because it becomes Middle-1 until it becomes R= <L which is L>R
    # Right Tree: Right will stay the same but Left will increase because it becomes Middle+1 until it becomes L= >R which is L>R
  
#SOLUTION 2
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
      if not nums: 
        return None 
      m = len(nums)//2
      root = TreeNode(nums[m])
      root.left = self.sortedArrayToBST(nums[:m])
      root.right = self.sortedArrayToBST(nums[m+1:])
      return root
#SUMMARY 2
#1 Unlike the previous solution we dont need a helper function because we dont set points, we simply modify the list parameter 
#2 We find the middle by doing len(nums)//2
#3 Set the middle to be the root node of the current tree/subtree 
#4 Now we set the Left tree to be the list up until the middle so nums[:m]
#5 We set the right tree to be the list from middle+1 till the end so nums[m+1:]
#6 Our Base case is an empty list which will happen when nums[-1,0] or nums[len(nums)+1:len(nums)]