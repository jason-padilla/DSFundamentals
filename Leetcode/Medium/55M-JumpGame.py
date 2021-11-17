'''
  You are given an integer array nums. 
  You are initially positioned at the array's first index, 
  and each element in the array represents your maximum jump length at that position.
  Return true if you can reach the last index, or false otherwise.
  Input: nums = [2,3,1,1,4]
  Output: true
  Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''
class Solution:
  def canJump(self, nums: List[int]) -> bool:
    if len(nums) == 1: return True
    if nums[0] == 0: return False
    jump = nums[0]-1
    idx = 1
    while idx < len(nums)-1:
      if nums[idx] == 0 and jump == 0:
        return False
      elif nums[idx] == 0:
        jump -= 1
        idx += 1
      else:
        jump = max(jump-1,nums[idx]-1)
        idx += 1
    return True