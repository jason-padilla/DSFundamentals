'''
  Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
  A subsequence of a string is a new string that is formed from the original string by 
  deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
  (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
  Input: s = "abc", t = "ahbgdc"    Input: s = "axc", t = "ahbgdc"
  Output: true                      Output: false
'''
class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    if len(s) > len(t): return False
    idx = 0
    for i in t:
      if idx < len(s) and i == s[idx]:
        idx += 1
    return len(s)== idx

#Summary 
#Simply go through the t and find the current char of s
#If s is a true subsequence of t the len of s and the val of idx will be the same
#If all the chars of s are there but not in the right order the values will be dif
#Because the current char can be at the end of t and as a result idx val will be less 
#The other chars of s wont be accounted for