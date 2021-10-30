'''
  Write a function that reverses a string. The input string is given as an array of characters s. 
  Input: s = ["h","e","l","l","o"]
  Output: ["o","l","l","e","h"]
'''

class Solution:
  def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    l, r = 0, len(s)-1
    while l < r:
      s[l], s[r] = s[r], s[l]
      l, r = l+1, r-1