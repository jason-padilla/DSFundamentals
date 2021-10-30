'''
  Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
  
  Input: s = "leetcode"   Input: s = "loveleetcode"   Input: s = "aabb"
  Output: 0               Output: 2                   Output: -1
'''

class Solution:
  def firstUniqChar(self, s: str) -> int:
    c = Counter(s)
    for i in range(len(s)):
      if c[s[i]] == 1:
        return i
    return -1