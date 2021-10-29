'''
  You are climbing a staircase. It takes n steps to reach the top.
  Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 
  
  Input: n = 2
  Output: 2
  Explanation: There are two ways to climb to the top.
  1. 1 step + 1 step
  2. 2 steps

  Input: n = 3
  Output: 3
  Explanation: There are three ways to climb to the top.
  1. 1 step + 1 step + 1 step
  2. 1 step + 2 steps
  3. 2 steps + 1 step
'''

#Brute Force
class Solution:
  def climbStairs(self, n: int) -> int:
    if n == 0:
      return 1
    if n < 0:
      return 0
    ones = self.climbStairs(n-1)
    twos = self.climbStairs(n-2)
    return ones + twos

#O(N) Dynamic Programming Memoization
class Solution:
  def climbStairs(self, n: int) -> int:
    one, two = 0, 1
    for i in range(n):
      one, two = two, one+two
    return two
#Summary 
#We add the previous two amounts to get to the next one 
#1 way to get to 0, 1 way to get to 1, 2 ways to get to 2 (1+1), 
  # 3 ways to get to 3 (1+2), 5 ways to get to 4(2+3), 8 ways to get to 5(3+5)