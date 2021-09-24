'''
  Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
  You must implement a solution with a linear runtime complexity and use only constant extra space.
  
  Example 1:
  Input: nums = [2,2,1]
  Output: 1
  
  Example 2:
  Input: nums = [4,1,2,1,2]
  Output: 4
  
  Example 3:
  Input: nums = [1]
  Output: 1 
'''
#Solution 1
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    map = Counter(nums) #Counter({2: 2, 1: 1})
    for i in map:
      if map[i] == 1:
        return i
#Summary
#1 Counter creates a hash table
#2 Just iterate through the values and return which has a count of 1

#Solution 2     
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)
#Summary 
#1 Simple mathematical solution 
#2 If we put the nums in a set we will only get individual values 
#3 Then we double the sum of the values
#4 We subtract the doubled sum by the sum of nums and we will get the individual remainder

#Solution 3
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    a = 0
    for i in nums:
        a ^= i
    return a
#Summary
#1 Manipulating the bits using XOR
#2 0 xor val = val
#3 val xor val = 0
#4 valA xor valB = valC, valA xor valC = valB, valC xor valB = valA
#5 The doubled values will cancel out to 0 and only the single value will be left out