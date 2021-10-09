'''
  Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
'''
class Solution:
  def addDigits(self, num: int) -> int:
    while num >= 10:
      num = (num//10)+(num%10)  
    return num 

class Solution(object):
  def addDigits(self, num):
    if num == 0:
        return 0
    return num % 9 or 9