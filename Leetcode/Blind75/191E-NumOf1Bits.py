
''' 
  191 NUMBER OF 1 BITS 
  Write a function that takes an unsigned integer and returns the number of '1' bits it has
  Input: n = 00000000000000000000000000001011
  Output: 3

  Input: n = 11111111111111111111111111111101
  Output: 31
''' 
class Solution:
  def hammingWeight(self, n: int) -> int:
    count = 0
    for i in range(32):
      bit = (n >> i) & 1
      if bit == 1:
        count += 1
    return count

#Summary 
#1 We can keep moving every digit to the 1s place by bit shifting by i 
#2 We then compare that 1s place digit and see if its a 1, if so increment the count

class Solution:
  def hammingWeight(self, n: int) -> int:
    count = 0
    while n:
      count += n&1
      n = n >> 1
    return count