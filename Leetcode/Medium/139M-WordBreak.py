'''
  Given a string s and a dictionary of strings wordDict, 
  return true if s can be segmented into a space-separated sequence of one or more dictionary words.
  Note that the same word in the dictionary may be reused multiple times in the segmentation.

  Input: s = "leetcode", wordDict = ["leet","code"]
  Output: true
  Explanation: Return true because "leetcode" can be segmented as "leet code".
'''

class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    dp = [False] * (len(s)+1)
    dp[-1] = True
    for i in range(len(s)-1,-1,-1):
      for w in wordDict:
        if i+len(w) <= len(s) and s[i:len(w)+i] == w:
          dp[i] = dp[i+len(w)]
        if dp[i]:
          break
    return dp[0]

#Summary 
#We want to check if from any idx a word exist in the wordDict
#The value will carry over 
#We want to iterate in reverse if the current idx+len of current word == word
#Then make the current idx = dp[i+len(w)] this will carry the value of True over
#If s can be broken up into words than dp[0] will be true