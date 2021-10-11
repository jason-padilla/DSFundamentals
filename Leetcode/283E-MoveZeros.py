'''
  Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
  Note that you must do this in-place without making a copy of the array. 
'''
class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    """ Do not return anything, modify nums in-place instead."""
    zero = 0
    for i in range(len(nums)):
      if nums[zero] == 0 and nums[i] != 0:
        nums[zero], nums[i] = nums[i], nums[zero]
      if nums[zero] != 0:
        zero +=1 
        