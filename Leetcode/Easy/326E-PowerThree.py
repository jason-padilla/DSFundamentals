'''
  Given an integer n, return true if it is a power of three. Otherwise, return false.
  An integer n is a power of three, if there exists an integer x such that n == 3x. 

  Input: n = 27   Input: n = 0    Input: n = 45
  Output: true    Output: false   Output: false
'''

class Solution:
  def isPowerOfThree(self, n: int) -> bool:
    target, p = 0, 0
    while target < n:
      target = 3**p
      if target == n: return True
      p += 1
    return False
#Summary 
# Iterate until target is either equal
# If target is greater than n than return False

class Solution:
  def isPowerOfThree(self, n: int) -> bool:
    p = 0
    while 3**p < n:
      p += 1
    return 3**p == n
#Summary 
# Iterate until 3**p is less than n
# Than check if 3**p is equal to n

class Solution:
  def isPowerOfThree(self, n: int) -> bool:
    max = 3**19
    return n > 0 and max%n == 0

#Summary
# Before this code we should figure out what the max power of 3 that is still less than 231 - 1
# We can do this by doing a while 3**p < 2**31-1 and find p
# Then we set that as the max and figure out if n > 0 and max%n == 0