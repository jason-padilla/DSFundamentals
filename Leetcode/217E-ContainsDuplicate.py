'''
  217 Contains Duplicate
  Given an integer array nums, return true if any value appears at least twice in the array, 
  and return false if every element is distinct.
'''
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    dix = {}
    for i in nums:
      if dix.get(i):
        return True
        dix[i] += 1
      else:
        dix[i] = 1
    return False
#Summary 
#1 We add the values from nums into a dict
#2 If the value is already in the dict than return True because that would mean there are duplicates

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    counted = Counter(nums)
    for i in counted.values():
      if i > 1:
        return True
    return False
#Summary 
#1 Faster way of putting the values of nums into a dict is using a Counter 
#2 If any of the values in the counter are greater than 1 return True

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)
#Summary 
#1 Simple short comparison, the set will have unique values if their are any duplicates the two lens wont equal