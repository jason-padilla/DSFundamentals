'''
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
  Input: pattern = "abba", s = "dog cat cat dog"
  Output: true

  Input: pattern = "abba", s = "dog cat cat fish"
  Output: false
'''
class Solution:
  def wordPattern(self, pattern: str, s: str) -> bool:
    words = s.split(" ")
    if len(words) != len(pattern): return False
    return len(set(zip(pattern,words))) == len(set(words)) == len(set(pattern))

#Summary
# First we want to split 's' into individual words that we can map
# Then we check if the len of the pattern and the words is equal
# If they are equal than we want to map each letter from the pattern with 1 one word from the 's'
# If each letter maps to only one letter than all of the lens will be equal 
# The set of map == set of pattern == set of words