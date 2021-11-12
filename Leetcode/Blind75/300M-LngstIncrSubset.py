'''
  Given an integer array nums, return the length of the longest strictly increasing subsequence.
  A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. 
  For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
  Input: nums = [10,9,2,5,3,7,101,18]
  Output: 4
  Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
'''

class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    dp = [1]*len(nums)
    for i in range(len(nums)-1,-1,-1):
      for j in range(i+1,len(nums)):
        if nums[i] < nums[j]:
          dp[i] = max(dp[i],1+dp[j])
    return max(dp)

#Summary 
#We iterate backwards and essentially check how many in front are greater
#The last value will be 1 because nothing is in front of it
#The second to last val can be either 1 or 2 weather i+1 is > than i
#We move backwards but check the values in front 
#We only change the val of our current index if the front index are less than curr and if they are greater
#Return the max number which will inidcate the longest subsequence