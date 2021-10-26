'''
  Given a sorted array of distinct integers and a target value, return the index if the target is found. 
  If not, return the index where it would be if it were inserted in order.
  You must write an algorithm with O(log n) runtime complexity.
  
  Input: nums = [1,3,5,6], target = 5
  Output: 2

  Input: nums = [1,3,5,6], target = 2
  Output: 1

  Input: nums = [1,3,5,6], target = 7
  Output: 4
'''

class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
      l, r = 0, len(nums)-1
      while l <= r:
        m = (l+r)//2
        if nums[m] == target:
          return m
        elif nums[m] < target:
          l = m+1
        elif nums[m] > target:
          r = m-1
      return l