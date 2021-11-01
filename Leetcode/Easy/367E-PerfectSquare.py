'''
  Given a positive integer num, write a function which returns True if num is a perfect square else False.
  Follow up: Do not use any built-in library function such as sqrt. 
  
  Input: num = 16   Input: num = 14
  Output: true      Output: false
'''
#Brute Force
class Solution:
  def isPerfectSquare(self, num: int) -> bool:
    count = 0
    while count*count <= num:
      if count*count == num:
        return True
      count += 1
    return False

#Binary Search
class Solution:
  def isPerfectSquare(self, num: int) -> bool:
    l, r = 0, num
    while l<=r:
      m = (l+r)//2
      if m*m == num:
        return True
      if m*m < num:
        l = m+1
      else:
        r = m-1
    return False