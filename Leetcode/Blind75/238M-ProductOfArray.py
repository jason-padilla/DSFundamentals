'''
  Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
  You must write an algorithm that runs in O(n) time and without using the division operation. 

  Input: nums = [1,2,3,4]
  Output: [24,12,8,6]
'''

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = []
    pre = 1
    for i in nums:
      res.append(pre)
      pre = pre*i 
    post = 1
    for i in range(len(nums)-1,-1,-1):
      res[i] = res[i]*post
      post = post * nums[i]
    return res

#Summary
#We make 1 pass through the arr and add the multiplication up until that point 
#Then we make a pass in the reverse order and multiply the prev val with whats in res
#This will give us the multiplication from the left and the right from the current idx without including it