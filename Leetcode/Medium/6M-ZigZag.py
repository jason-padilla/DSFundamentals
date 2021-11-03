'''
  The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
  (you may want to display this pattern in a fixed font for better legibility)
  Input: s = "PAYPALISHIRING", numRows = 3
    P   A   H   N
    A P L S I I G
    Y   I   R
  Output: "PAHNAPLSIIGYIR"

  Input: s = "PAYPALISHIRING", numRows = 4
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
  "PINALSIGYAHRPI"
'''

class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if len(s) == 1 or numRows == 1: return s
    rows = [[] for i in range(numRows)]
    idx = 0
    mid = False
    for c in s:
      if mid and idx > 0:
        rows[idx].append(c)
        idx -= 1
      else:
        mid = False
        rows[idx].append(c)
        idx += 1
        if idx == numRows:
          idx -= 2
          mid = True
    res = ''
    for l in rows:
      res += ''.join(l)
    return res

#Summary
#We want to make 2d array that reprent each row to put the values in 
#Iterate throught the string and add the current char to the dedicated row based on the idx
#If the idx == numRows then the the next chars will be added to the middle cols which represent the zig zag 
#Instead of incrementing we will now decrement
#Decrement until the idx reaches 0, at which point we will go back to a normal col and start incrementing
#Finally join all of the chars into strings and concat them into a final string