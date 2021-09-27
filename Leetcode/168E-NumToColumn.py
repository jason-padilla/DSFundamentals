''' 
  168 Excel Sheet Column Title 
  Given an integer columnNNumber return its corresponding column title as it appears in an Excel sheet.
  Example 1:
  Input: columnNumber = 1
  Output: "A"

  Example 2:
  Input: columnNumber = 28
  Output: "AB"
  
  Example 3:
  Input: columnNumber = 701
  Output: "ZY"
  
  Example 4:
  Input: columnNumber = 2147483647
  Output: "FXSHRXW"
'''

class Solution:
  def convertToTitle(self, columnNumber: int) -> str:
    result = ""
    while columnNumber:
      result += chr(ord('A') + (columnNumber-1) % 26)
      columnNumber = (columnNumber-1) // 26
    return result[::-1]

#Summary 
#1 Letters are 1-26 and if we take the modulo of a value we get the remainder
#2 The remainder will give us the tail value which can be converted to a letter
#3 We subtract 1 so that say we wanted 'A' we add 'A' + 0 = 'A' instead of 'A'+ 1 != 'A'
#4 Then we divide the number by 26 to decrement the number and finally return the reverse order
