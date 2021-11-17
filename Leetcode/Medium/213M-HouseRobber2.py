'''
  You are a professional robber planning to rob houses along a street. 
  Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
  That means the first house is the neighbor of the last one. 
  Meanwhile, adjacent houses have a security system connected, 
  and it will automatically contact the police if two adjacent houses were broken into on the same night.
  Given an integer array nums representing the amount of money of each house, 
  return the maximum amount of money you can rob tonight without alerting the police.
  Input: nums = [2,3,2]
  Output: 3
  Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
'''
class Solution:
  def rob(self, nums: List[int]) -> int:
    if len(nums) <= 2:
      return max(nums)
    rob1 = rob2 = 0
    for i in nums[1:]:
      rob1, rob2 = rob2, max(rob1+i,rob2)
    rob3 = rob4 = 0
    for i in nums[:-1]:
      rob3, rob4 = rob4, max(rob3+i,rob4)
    return max(rob2,rob4)