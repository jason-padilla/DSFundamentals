'''
  Given a string s, find the length of the longest substring without repeating characters.
  
  Input: s = "abcabcbb"
  Output: 3
  Explanation: The answer is "abc", with the length of 3.

  Input: s = "pwwkew"
  Output: 3
  Explanation: The answer is "wke", with the length of 3.
  Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
  
  Input: s = "bbbbb"
  Output: 1
  Explanation: The answer is "b", with the length of 1.
'''

class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    curr = set()
    p = longest = 0
    for i in range(len(s)):
      while s[i] in curr:
        curr.remove(s[p])
        p += 1
      curr.add(s[i])
      longest = max(longest,len(curr))
    return longest

#Summary 
#Sliding window technique, we are using sets because the access time is constant 
#We want to have a pointer that indicates the start of the current substring
#The value is the index in our main string 
#If the value we want to add is already in our set we want to remove the values from the set up to that point
#We do this to avoid going completely back; ex: i = "c" set = "abcde" we remove "abc" and make set "dec"
#We then make longest = the greater value of either an already existing substring or the current substring 