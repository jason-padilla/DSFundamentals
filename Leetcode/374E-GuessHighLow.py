'''
  We are playing the Guess Game. The game is as follows:
  I pick a number from 1 to n. You have to guess which number I picked.
  Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
  You call a pre-defined API int guess(int num), which returns 3 possible results:
  -1: The number I picked is lower than your guess (i.e. pick < num).
  1: The number I picked is higher than your guess (i.e. pick > num).
  0: The number I picked is equal to your guess (i.e. pick == num).
  Return the number that I picked. 
  #Wording is confusing but its a binary search problem
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
  def guessNumber(self, n: int) -> int:
    l, r = 1, n
    while l<=r:
      m = (l+r)//2
      g = guess(m)
      if 0 == g:
        return m
      elif 0 > g:
        r = m-1
      else:
        l = m+1
    return l