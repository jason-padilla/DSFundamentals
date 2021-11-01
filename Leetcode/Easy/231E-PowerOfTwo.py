'''
  Given an integer n, return true if it is a power of two. Otherwise, return false.
  An integer n is a power of two, if there exists an integer x such that n == 2^x.
'''

class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    count = 0
    while 2**count != n:
      if 2**count > n:
        return False
      count += 1
    return True

class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    return not n&n-1 if n else False