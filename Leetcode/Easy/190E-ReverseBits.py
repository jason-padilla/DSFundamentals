'''
  190 REVERSE BITS
  Reverse bits of a given 32 bits unsigned integer. 
  Input: n = 00000010100101000001111010011100
  Output:    964176192 (00111001011110000010100101000000)
'''
class Solution:
  def reverseBits(self, n: int) -> int:
    res = 0
    for i in range(32):
      bit = (n >> i) & 1
      res = res | bit << (31-i)
    return res

#Summary 
#1 We want to loop over the 32 bit binay number and get the first value and put it at front of res 
#2 We can do this by bit shifting n by i. We shift by 0 we get the 1s place, shift by 1 we get 10s and so on
#3 We and it so that we get either 1 or 0 
#4 Once we get that individual value we OR it to res by shifting bit by 31-i