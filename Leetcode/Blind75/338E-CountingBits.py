'''
  Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
  ans[i] is the number of 1's in the binary representation of i.

  Input: n = 2
  Output: [0,1,1]
  Explanation:
  0 --> 0
  1 --> 1
  2 --> 10

  Input: n = 5
  Output: [0,1,1,2,1,2]
  Explanation:
  0 --> 0
  1 --> 1
  2 --> 10
  3 --> 11
  4 --> 100
  5 --> 101
'''

#Bit Shifting O(n^2)
class Solution:
  def countBits(self, n: int) -> List[int]:
    res = []
    for i in range(n+1):
      count = 0
      while i:
        count += i&1
        i = i>>1
      res.append(count)
    return res

#Better DP solution
class Solution:
  def countBits(self, n: int) -> List[int]:
    dp = [0]
    offset = 1
    for i in range(1,n+1):
      if offset * 2 == i:
        offset = i 
      dp.append(1+dp[i-offset])
    return dp
#Summary
# We are using dynamic programming and building off the previous results 
# Most significant bits in binary are powers of 2 so 1,2,4,8,16,32...
# Every new significant bit it has a new 1, 10 = 2, 100=4, 1000=8 
# If we do 1+dp[i-offset] it will give us 1(significant)+i-offset which will give us 1+[i-offset/2]
