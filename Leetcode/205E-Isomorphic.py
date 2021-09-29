'''
  205. Isomorphic Strings
  Given two strings s and t, determine if they are isomorphic.
  Two strings s and t are isomorphic if the characters in s can be replaced to get t.
  All occurrences of a character must be replaced with another character while preserving the order of characters. 
  No two characters may map to the same character, but a character may map to itself.
  
  Example 1:
  Input: s = "egg", t = "add"
  Output: true
  
  Example 2:
  Input: s = "foo", t = "bar"
  Output: false
  
  Example 3:
  Input: s = "paper", t = "title"
  Output: true
'''
class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    dix = {}
    for i in range(len(s)):
      if s[i] not in dix:
        if t[i] not in dix.values():
          dix[s[i]] = t[i]
        else:
          return False
      else:
        if dix[s[i]] != t[i]:
          return False
    return True
#Summary 
#1 Add a every char from s to dix and map it to a t char
#2 Only add it if the s char has not been in the char before
#3 If it hasnt been in the dix than add it but only if t char isnt in .values 
#4 If it is, make sure that the valued mapped to it is equal to the t char 
#5 Time: Worst Cubic Best Linear, Space: Linear
 
class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    dix = {}
    for i in range(len(s)):
      try:
        if dix[s[i]] != t[i]:
          return False
      except:
        if t[i] not in dix.values():
          dix[s[i]] = t[i]
        else:
          return False
    return True
#Summary 
#1 Add a every char from s to dix and map it to a t char
#2 Only add it if the s char has not been in the char before
#3 If it hasnt been in the dix than add it but only if t char isnt in .values 
#4 If it is, make sure that the valued mapped to it is equal to the t char 
#5 Time: Worst Quadratic Best Linear, Space: Linear

class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    m1, m2 = [0]*256, [0]*256
    for i in range(len(s)):
      if m1[ord(s[i])] != m2[ord(t[i])]:
        return False
      m1[ord(s[i])] = i+1
      m2[ord(t[i])] = i+1
    return True
#Summary 
#1 All of the chars are within ASCII so max len we need to make lists is 256
#2 We compare the values paired to each other 
#3 If they dont match than we return false
#4 This works because the pairs will icrement by the same amount 
  # But if a letter is paired to a different letter than originally than increments will be different 
#5 Time: Linear, Space: Linear