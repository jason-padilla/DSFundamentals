'''
  Given an array of distinct integers nums and a target integer target, 
  return the number of possible combinations that add up to target.
  The answer is guaranteed to fit in a 32-bit integer.

  Input: nums = [1,2,3], target = 4
  Output: 7
  Explanation:
  The possible combination ways are:
  (1, 1, 1, 1)
  (1, 1, 2)
  (1, 2, 1)
  (1, 3)
  (2, 1, 1)
  (2, 2)
  (3, 1)
  Note that different sequences are counted as different combinations.
'''
class Solution:
  def combinationSum4(self, nums: List[int], target: int) -> int:
    dp = {0:1}
    for i in range(1,target+1):
      dp[i] = 0
      for n in nums:
        dp[i] += dp.get(i-n,0)
    return dp[target]

#Summary
#From the current value subtract the n in nums
#This will give you how many ways that can sum up to the current value