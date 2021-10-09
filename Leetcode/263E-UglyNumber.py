'''
  An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
  Given an integer n, return true if n is an ugly number.
  
  Input: n = 6
  Output: true
  Explanation: 6 = 2 × 3

  Input: n = 8
  Output: true
  Explanation: 8 = 2 × 2 × 2

  Input: n = 14
  Output: false
  Explanation: 14 is not ugly since it includes the prime factor 7.
'''
class Solution:
  def isUgly(self, n: int) -> bool:
    for p in [2, 3, 5]:
      while (n % p == 0) and (0 < n):
        n /= p
    return n == 1