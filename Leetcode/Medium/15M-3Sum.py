'''
  Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
  Notice that the solution set must not contain duplicate triplets. 
  
  Input: nums = [-1,0,1,2,-1,-4]
  Output: [[-1,-1,2],[-1,0,1]]
'''
class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = [] 
    if len(nums) < 3: return res
    nums.sort()
    for i in range(len(nums)):
      if i > 0 and nums[i] == nums[i-1]:
        continue
      l, r = i+1, len(nums)-1
      while l < r:
        curr = nums[i]+nums[l]+nums[r]
        if curr > 0:
          r -= 1
        elif curr < 0:
          l += 1
        else:
          res.append([nums[i],nums[l],nums[r]])
          l += 1
          while l<r and nums[l] == nums[l-1]:
            l+= 1
    return res