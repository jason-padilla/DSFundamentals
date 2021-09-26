'''
  167 Two Sum II - Input array is sorted
  Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
  find two numbers such that they add up to a specific target number. 
  Let these two numbers be numbers[index1] and numbers[index2] where 1 <= first < second <= numbers.length.
  Return the indices of the two numbers, index1 and index2, as an integer array [index1, index2] of length 2.
  The tests are generated such that there is exactly one solution. You may not use the same element twice.
'''

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    dix = {}
    for i in range(len(numbers)):
      diff = target - numbers[i]
      if diff in dix:
        first = dix[diff]
        return [first,i+1]
      else:
        dix[numbers[i]] = i+1
#Summary 
#1 Use a hashtable to include the values we have already seen 
#2 We try to look for the value diff between target and curent val
#3 Doing so we can find the two values that add up to the target value
#4 Time: Quadratic, Space: Linear
class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    dix = {}
    for i in range(len(numbers)):
      diff = target - numbers[i]
      try:
        first = dix[diff]
        return [first,i+1]
      except:
        dix[numbers[i]] = i+1
#Summary 
#1 Use a hashtable to include the values we have already seen 
#2 We try to look for the value diff between target and curent val
#3 Doing so we can find the two values that add up to the target value
#4 Time: Linear, Space: Linear

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l,r = 0, len(numbers)-1
    while l < r:
      if numbers[l]+numbers[r] == target:
        return [l+1,r+1]
      elif numbers[l]+numbers[r] > target:
        r -= 1
      else:
        l += 1
#Summary 
#1 Use a two pointer method, left at the start and right at the end 
#2 If the two values equal return the index
#3 If the sum of two values is greater than target decrement right
#4 If the sum of two values is lesser than target increment left
#5 Time: Linear, Space: Constant