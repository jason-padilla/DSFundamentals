''' 
  Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. 

  Input: s = "III"
  Output: 3 

  Input: s = "IX"
  Output: 9

  Input: s = "LVIII"
  Output: 58
  Explanation: L = 50, V= 5, III = 3.
'''

class Solution:
  def romanToInt(self, s: str) -> int:
    converter = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    result = converter[s[0]]
    for i in range(1,len(s)):
      previous = converter[s[i-1]]
      current = converter[s[i]]
      if previous < current:
        result -= previous * 2
      result += current
    return result

#Summary: 
#0 Key: subtract will happen when prev < curr
#1 Start iterating from the left
#2 Check if the prev value is less than the current val
#3 If so subtract prev*2 from res 
#4 Add the current val to res 