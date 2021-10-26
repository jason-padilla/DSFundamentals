'''
  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
  You may assume that each input would have exactly one solution, and you may not use the same element twice.
  You can return the answer in any order.

  Input: nums = [2,7,11,15], target = 9
  Output: [0,1]
  Output: Because nums[0] + nums[1] == 9, we return [0, 1].

  Input: nums = [3,2,4], target = 6
  Output: [1,2]
''' 
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    dix = {} 
    for i in range(len(nums)):
      diff = target-nums[i]
      if diff in dix:
        return [dix[diff],i]
      else:
        dix[nums[i]] = i
#Summary
#1 Iterate through the nums and check if target-curr is in dix
#2 If it is than that means those are the two vals that add up to target 
#3 If it isnt in dix than add curr to dix with the idx