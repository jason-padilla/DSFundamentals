'''
  Given a string s, reverse only all the vowels in the string and return it.
  The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

  Input: s = "hello"  Input: s = "leetcode"
  Output: "holle"     Output: "leotcede"
'''
class Solution:
  def reverseVowels(self, s: str) -> str:
    l, r = 0, len(s)-1
    s = list(s)
    vowels = set('aeiouAEIOU')
    while l < r:
      if s[l] in vowels and s[r] in vowels:
        s[l], s[r] = s[r], s[l]
        l, r = l+1, r-1
      elif s[l] in vowels:
        r-=1
      elif s[r] in vowels:
        l+=1
      else:
        l, r = l+1, r-1
    return ''.join(s)

#Summary 
#Same as reversing a string normally but we only move if either l or r is a vowel 
#We use a set to store vowels because acces to set is in constant time