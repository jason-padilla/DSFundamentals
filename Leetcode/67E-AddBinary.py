'''
  Given two binary strings a and b, return their sum as a binary string.
  Input: a = "11", b = "1"    Input: a = "1010", b = "1011"
  Output: "100"               Output: "10101"
'''

#Convert To Binary
class Solution:
  def addBinary(self, a: str, b: str) -> str:
    result = int(a,2) + int(b,2)
    result = bin(result)
    return result[2:]

#Long Conversion
class Solution:
  def addBinary(self, a: str, b: str) -> str:
    pA, pB = len(a)-1, len(b)-1
    result = ''
    carry = 0
    while pA > -1 or pB > -1:
      if pA < 0:
        res = self.helper(0,b[pB],carry)
        result, carry = str(res[0])+result, res[1]
        pB -= 1
      elif pB < 0: 
        res = self.helper(a[pA],0,carry)
        result, carry = str(res[0])+result, res[1]
        pA -= 1
      else:
        res = self.helper(a[pA],b[pB],carry)
        result, carry = str(res[0])+result, res[1]
        pA, pB = pA-1, pB-1
    if carry:
      return '1' + result
    return result
        
  def helper(self, a: str, b: str, carry: int) -> []:
    if int(a)+int(b)+carry == 2:
      return [0,1]
    elif int(a)+int(b)+carry == 3:
      return [1,1]
    else:
      return [int(a)+int(b)+carry,0]

#Using a Stack
class Solution:
  def addBinary(self, a: str, b: str) -> str:
    a = list(a)
    b = list(b)
    result = ''
    carry = 0
    while a or b:
      if a:
        carry += int(a.pop())
      if b:
        carry += int(b.pop())
      result = str(carry%2) + result
      carry //= 2
    if carry:
      return '1' + result
    return result