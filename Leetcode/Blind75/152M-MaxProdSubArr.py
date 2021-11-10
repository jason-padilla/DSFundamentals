'''
  Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
  It is guaranteed that the answer will fit in a 32-bit integer.
  A subarray is a contiguous subsequence of the array. 

  Input: nums = [2,3,-2,4]
  Output: 6
  Explanation: [2,3] has the largest product 6.
'''
class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    res = currMin = currMax = nums[0]
    for i in nums[1:]:
      temp = currMax * i
      currMax = max(currMin*i, currMax*i, i)
      currMin = min(currMin*i, temp, i)
      res = max(currMax,currMin,res)
    return res

#Summary 
#When all of the numbers are positive the subarray will grow
#If negative numbers exist the max value can alterante between positive and negative
#The max val can be between two negatives
#Due to this we should also keep track of the min val 
#Ex: [-1,-2,-3] max = 6 (-2,-3)