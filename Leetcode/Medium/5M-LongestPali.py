'''
  Given a string s, return the longest palindromic substring in s.
  Input: s = "babad"  Input: s = "cbbd"   Input: s = "a"
  Output: "bab"       Output: "bb"        Output: "a"
'''

class Solution:
  def longestPalindrome(self, s: str) -> str:
    res = ''
    for i in range(len(s)):
      l = r = i
      while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
        if len(s[l:r+1]) > len(res):
          res = s[l:r+1]
        l, r = l-1, r+1
      l, r = i, i+1
      while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
        if len(s[l:r+1]) > len(res):
          res = s[l:r+1]
        l, r = l-1, r+1
    return res

#Condensed
class Solution:
  def longestPalindrome(self, s: str) -> str:
    def helper(l,r) -> str:
      while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
        l, r = l-1, r+1
      return s[l+1:r]
    res = ''
    for i in range(len(s)):
      res = max(res, helper(i,i), helper(i,i+1), key=lambda x: len(x))
    return res

#Summary 
#We usually find palindromes by moving left and right inward but in this case we move outward
#We keep checking to see if from our current char we can have a valid palindrome
#We change the res based on if the len of the new palindrome is longer than the prev
#We check for two conditions: odd palindromes "aba" and even palindromes "abba"
#The longest one will be returned