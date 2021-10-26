'''
  Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
  A subarray is a contiguous part of an array. 

  Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
  Output: 6
  Explanation: [4,-1,2,1] has the largest sum = 6.

  Input: nums = [5,4,-1,7,8]
  Output: 23
'''

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    largest = nums[0]
    current = nums[0]
    for i in nums[1:]:
      if current+i < i:
        current = i
      else:
        current += i
      largest = max(largest,current)
    return largest
#Summary
#1 Idea is to keep adding to the current max if adding is > i 
  #else make current = i 