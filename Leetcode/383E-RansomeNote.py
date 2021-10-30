'''
  Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
  Each letter in magazine can only be used once in ransomNote.

  Input: ransomNote = "a", magazine = "b"
  Output: false

  Input: ransomNote = "aa", magazine = "ab"
  Output: false

  Input: ransomNote = "aa", magazine = "aab"
  Output: true
'''

class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    c = Counter(magazine)
    for i in ransomNote:
      if i in c:
        if c[i] <= 0:
          return False
        c[i] -= 1
      else:
        return False
    return True
#Summary 
#Make a dict out of the magazine
#ransomNote can be made out of magazine if it has all of the values 
#We check that by making sure the value exist in the dict and its count doesnt < 0

#Condensed Fun Way
class Solution(object):
  def canConstruct(self, ransomNote, magazine):
    c1, c2 = collections.Counter(ransomNote), collections.Counter(magazine)
    return all(k in c2 and c2[k]>=c1[k] for k in c1)
#Summary 
#Make dicts for both strings 
#Check to see that for every char in c1 it is in c2 and the amount of times it appears isnt greater in c2
#All method returns True if all of the values inside are True else returns False