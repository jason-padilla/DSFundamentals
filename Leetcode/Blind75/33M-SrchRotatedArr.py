'''
  There is an integer array nums sorted in ascending order (with distinct values).
  Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
  such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
  For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
  Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
  You must write an algorithm with O(log n) runtime complexity.

  Input: nums = [4,5,6,7,0,1,2], target = 0
  Output: 4

  Input: nums = [4,5,6,7,0,1,2], target = 3
  Output: -1
'''

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums)-1
    while l <= r:
      m = (l+r)//2
      if nums[m] == target:
        return m
      elif nums[l] <= nums[m]:
        if nums[l] <= target <= nums[m]:
          r = m-1
        else:
          l = m+1
      else:
        if nums[m] <= target <= nums[r]:
          l = m+1
        else:
          r = m-1
    return -1

#Summary 
#A more advance version of binary search 
#Since the list is sorted but rotated we need to 
  # check on what side is less and what side is more
#Then we need to check that the target is within that range
#If not switch sides and keep checking until targetr is found