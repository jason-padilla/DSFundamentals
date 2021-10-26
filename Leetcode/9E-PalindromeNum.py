'''
  Given an integer x, return true if x is palindrome integer.
  An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not. 
  
  Input: x = 121
  Output: true

  Input: x = -121
  Output: false
  Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

  Input: x = 10
  Output: false
  Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

class Solution:
  def isPalindrome(self, x: int) -> bool:
    if x < 0: return False
    s = str(x)
    l,r = 0, len(s)-1
    while l < r:
      if s[l] != s[r]:
        return False
      l, r = l+1, r-1
    return True
#Summary 
#1 Simple solution converting to string and then comparing if l == r

class Solution:
  def isPalindrome(self, x: int) -> bool:
    if x < 0:
      return False 
    inverted = 0
    original = x
    while x > 0:
      inverted *= 10
      inverted += (x%10)
      x = x//10
    return inverted == original  
#Summary 
#1 If x < 0 it cant be a palindrome 
#2 Remove every digit from x and add it to inverted 
#3 We do this by getting the remainder x%10
#4 lastly compare if the inverted number is equal to the orginal 