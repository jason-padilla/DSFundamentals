'''
  Write a function to find the longest common prefix string amongst an array of strings.
  If there is no common prefix, return an empty string "".

  Input: strs = ["flower","flow","flight"]
  Output: "fl"

  Input: strs = ["dog","racecar","car"]
  Output: ""
'''

class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    res = ''
    for i in range(len(strs[0])):
      for s in strs:
        if i == len(s) or s[i] != strs[0][i]:
          return res
      res += strs[0][i]
    return res

#Summary 
#1 Longest prefix will be when we find a char that doesnt equal the rest
#2 We can start looping through the chars of the first str as a reference
#3 Then we loop through all of the strings in strs and compare the current index of each one 
  #to the index of the char we are on 
#4 If one of the strings is shorter than the rest we prevent going out of boudns by comparing
  #if the current i is equal to the len() of the current string we are on
#5 Add the current char to the res