'''
  You have n coins and you want to build a staircase with these coins. 
  The staircase consists of k rows where the ith row has exactly i coins. 
  The last row of the staircase may be incomplete.
  Given the integer n, return the number of complete rows of the staircase you will build. 
  c                                   c
  cc                                  cc
  ccx                                 ccc
                                      ccxx
  Input: n = 5                        Input: n = 8
  Output: 2                           Output: 3
  Explanation: 3rd row is incomplete. Explanation: 4th row is incomplete.
'''
#Brute Force
class Solution:
  def arrangeCoins(self, n: int) -> int:
    count = 1
    while (n - count) >= 0:
      n -= count
      count += 1
    return count - 1
    
#Binary Search
class Solution:
  def arrangeCoins(self, n: int) -> int:
    left, right = 0, n
    while left <= right:
      k = (right + left) // 2
      curr = k * (k + 1) // 2
      if curr == n:
        return k
      if n < curr:
        right = k - 1
      else:
        left = k + 1
    return right