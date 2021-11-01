'''
  171 Excel Sheet Column Number
  Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
  Example 1:
  Input: columnTitle = "A
  Output: 1

  Example 2:
  Input: columnTitle = "AB
  Output: 28

  Example 3:
  Input: columnTitle = "ZY"
  Output: 701

  Example 4:
  Input: columnTitle = "FXSHRXW"
  Output: 2147483647
'''

class Solution:
  def titleToNumber(self, columnTitle: str) -> int:
    result = 0
    for i in columnTitle:
      result = 1 + (result*26) + (ord(i)-65) % 26
    return result
#Summary
#1 Go through each letter and add it to result
#2 We add 1 because its 1-indexed (e.g. A==1 != 0) 
  # we multiple by the previous value and 26 because every letter is a new 26
  # get the ord and - 65 because 65 is the ord val of A and we want to start at 1
  # mod 26 to get the remainder 