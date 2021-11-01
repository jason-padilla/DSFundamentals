'''
  202 HAPPY NUMBER 
  Write an algorithm to determine if a number n is happy.
  A happy number is a number defined by the following process:
  Starting with any positive integer, replace the number by the sum of the squares of its digits.
  Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
  Those numbers for which this process ends in 1 are happy.
  Return true if n is a happy number, and false if not.
  
  Input: n = 19
  Output: true
  Explanation:
  12 + 92 = 82
  82 + 22 = 68
  62 + 82 = 100
  12 + 02 + 02 = 1
'''

class Solution:
  def isHappy(self, n: int) -> bool:
    if n == 1: return True
    split = list(str(n))
    seen = set()
    while n != 1:
      n=0
      for i in split:
        n += int(i)**2
      if n == 1: return True
      if n in seen: return False
      split = list(str(n))
      seen.add(n)
#Summary: Using a str
#1 Use a string and a list to split the current number individually 
#2 Reset the value to 0 so we can perform an operation to it 
#3 Perform the square sum to the numbers in the list 
#4 If it sums up to 1 than return True 
#5 If sum has already been in the set than return False
  #If it has already been there that means there is a cycle 
#6 If it hasnt been in the set add it

class Solution:
  def isHappy(self, n: int) -> bool:
    seen = set()
    if n == 1: return True
    while n != 1:
      n = self.squareSum(n)
      if n == 1: return True 
      elif n in seen: return False
      else: seen.add(n)
    
  def squareSum(self, n: int) -> int:
    res = 0
    while n:
      res += (n%10)**2
      n = n//10
    return res

#Summary: Using Math
#1 Using the modulo operator we can pick out the individual values and get our sum
#2 Reset the value to 0 so we can perform an operation to it 
#4 If it sums up to 1 than return True 
#5 If sum has already been in the set than return False
  #If it has already been there that means there is a cycle 
#6 If it hasnt been in the set add it

class Solution:
  def isHappy(self, n: int) -> bool:
    slow = self.squareSum(n)
    fast = self.squareSum(self.squareSum(n))
    while slow!=fast and fast!= 1:
      slow = self.squareSum(slow)
      fast = self.squareSum(self.squareSum(fast))
    return fast == 1
  def squareSum(self, n: int) -> int:
    res = 0
    while n:
      res += (n%10)**2
      n = n//10
    return res

#Summary: Using Fast Slow
#1 Using the modulo operator we can pick out the individual values and get our sum
#2 We can use the two pointer fast and slow technique 
#3 As long as slow and fast arent equal than keep performing the operation 
  #This is used to detect if there is a cycle
#4 Once out of the loop compare if fast == 1
