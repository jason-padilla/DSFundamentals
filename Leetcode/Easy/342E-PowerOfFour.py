'''
  Given an integer n, return true if it is a power of four. Otherwise, return false.
  An integer n is a power of four, if there exists an integer x such that n == 4x.
  Input: n = 16   Input: n = 5    Input: n = -123
  Output: true    Output: false   Output: false
'''

#Mathematical
class Solution:
  def isPowerOfFour(self, n: int) -> bool:
    return n>0 and log(n,4).is_integer()

#Brute Force
class Solution:
  def isPowerOfFour(self, n: int) -> bool:
    while n>1:
      n = n/4
    return n == 1