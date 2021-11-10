#O(log n)
class Solution:
  def findMin(self, nums: List[int]) -> int:
    l, r = 0, len(nums)-1
    minVal = nums[0]
    while l <= r:
      m = (l+r)//2
      if nums[m] >= minVal:
        l = m+1
      else:
        minVal = nums[m]
        r = m-1
    return minVal