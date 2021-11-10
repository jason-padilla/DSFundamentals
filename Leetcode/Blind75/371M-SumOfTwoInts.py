'''
  Given two integers a and b, return the sum of the two integers without using the operators + and -.
  Input: a = 1, b = 2
  Output: 3

  Input: a = 2, b = 3
  Output: 5
'''
class Solution:
  def getSum(self, a: int, b: int) -> int:
    mask = 0xffffffff
    while (b & mask):
      carry = (a & b) << 1
      a = a ^ b
      b = carry
    if b > 0:
      return (a & mask)
    else:
      return a

#Short 
class Solution:
  def getSum(self, a: int, b: int) -> int:
    mask = 0xffffffff
    while (b & mask):
      a, b = a ^ b, (a & b) << 1
    return (a & mask) if b else a 

#Summary 
#To add without actually adding we need to logicgate the integers bits 
#If we xor the integers we can essentially add them but it doesnt include a carry
#So we also need to and the values and place the carry in a seperate value
#We continue to xor and & as long as the carry is 1