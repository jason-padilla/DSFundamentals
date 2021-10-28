'''
  Given a non-negative integer x, compute and return the square root of x.
  Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
  Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5. 
  
  Input: x = 4  Input: x = 8
  Output: 2     Output: 2
'''

class Solution:
  def mySqrt(self, x: int) -> int:
      result = 0
      count = 0
      while (count * count) <= x:
        count += 1
      return count-1
      
class Solution:
  def mySqrt(self, x: int) -> int:
    if x < 2:
      return x
    left, right = 2, x
    while left < right:
      mid = (left+right)//2
      if mid*mid == x: return mid
      elif mid*mid > x: right = mid
      elif mid*mid < x: left = mid + 1
    return left - 1