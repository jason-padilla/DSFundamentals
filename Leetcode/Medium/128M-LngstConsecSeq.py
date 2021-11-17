'''
  Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
  You must write an algorithm that runs in O(n) time.
  
  Input: nums = [100,4,200,1,3,2]
  Output: 4
  Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''
class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    if len(nums) == 0: return 0
    uni = set(nums)
    longest = 0 
    for i in nums:
      if i-1 not in uni:
        count = 1
        while i+count in uni:
          count += 1
        longest = max(longest,count)
    return longest