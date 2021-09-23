'''
  Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
  Input: s = "A man, a plan, a canal: Panama"
  Output: true
  Explanation: "amanaplanacanalpanama" is a palindrome.
'''
 
class Solution:
  def isPalindrome(self, s: str) -> bool:
      left = 0
      right = len(s) - 1
      while left < right:
          if s[left].isalnum():
              if s[right].isalnum():
                  if s[left].upper() == s[right].upper():
                      left += 1
                      right -= 1
                  else:
                      return False
              else:
                  right -= 1
          else:
              left += 1
      return True

#SUMMARY 
#1 We want two pointers left at start and right at end
#2 We will make sure it is a alpha num char if not increase its index by 1
#3 If both left and right are alpha num compare them to see if theyre equal