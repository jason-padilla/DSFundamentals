'''
  Implement strStr().
  Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

  Input: haystack = "hello", needle = "ll"
  Output: 2

  Input: haystack = "aaaaa", needle = "bba"
  Output: -1

  Input: haystack = "", needle = ""
  Output: 0
''' 
class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
      if len(needle) == 0: return 0
      if len(needle) > len(haystack): return -1
      for i in range(len(haystack)):
        end = len(needle) + i
        if haystack[i:end] == needle:
          return i
      return -1