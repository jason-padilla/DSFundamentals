'''
  You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
  The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
  Increment the large integer by one and return the resulting array of digits.
  
  Input: digits = [1,2,3]
  Output: [1,2,4]
  Explanation: The array represents the integer 123.
  Incrementing by one gives 123 + 1 = 124.
  Thus, the result should be [1,2,4].
'''

#String Solution
class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    num = 0
    tens = 1
    for i in range(len(digits)-1,-1,-1):
      num += digits[i]*tens
      tens *= 10
    num += 1
    return list(str(num))

#No String Conversion
class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    carry = 1
    for i in range(len(digits)-1,-1,-1):
      if digits[i] + carry > 9:
        digits[i] = 0
        carry = 1
      else:
        digits[i] += carry
        carry = 0
    if carry: 
      return [1]+digits
    return digits