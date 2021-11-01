'''
  Given an array nums of size n, return the majority element.
  The majority element is the element that appears more than ⌊n / 2⌋ times. 
  You may assume that the majority element always exists in the array.

  Example 1:
  Input: nums = [3,2,3]
  Output: 3
  
  Example 2:
  Input: nums = [2,2,1,1,1,2,2]
  Output: 2
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
#Summary 
#1 Sort the values and get the middle value which will be the majority
#2 Time: linear * log, Space: Linear

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    dix = {}
    for i in nums:
      dix[i] = dix.get(i,0) + 1
      if dix[i] > len(nums)//2:
        return i
#Summary 
#1 Put the values in a hash table and find the one with i > n//2
#2 Time: Quadratic, Space: Linear

class Solution:
  def majorityElement(self, nums: List[int]) -> int: 
    counter = 0
    elm = None  
    for i in nums:
      if counter == 0:
        elm = i
        counter += 1
      elif elm == i:
        counter += 1
      else:
        counter -= 1
    return elm
#Summary 
#1 Pass through the values with a counter and majority elm
#3 Increment if the current value is equal to the majority elm else decrement
#4 If the majority elm reaches 0 replace it with a new majority elm
#2 Time: Linear, Space: Constant