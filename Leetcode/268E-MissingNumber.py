'''
  268 MISSING NUMBER
  Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''
class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    target = factorial(len(nums))
    zero = False
    for i in nums:
      if i:
        target = target//i
      else:
        zero = True 
    if not zero: return 0
    return target
#Summary 
# Create a factorial of the len of the nums
# Iterate through the nums and divide it from the factorial 
# If the current num is zero mark that zero has been seen 
# At the end check if zero has been seen 
# Else return the missing value

class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    target = sum(nums)
    for i in range(len(nums)+1):
      target -= i
      if target < 0:
        return abs(target)
    return target
#Summary 
# Get the sum of values 
# Iterate throught the values of the len of nums
# Subtract the current index from the target
# If the result is less than 0 thats the missing number
# If it reaches outside of the loop that means the only number missing was the zero

class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    return len(nums)*(len(nums)+1)//2 - sum(nums)

#Summary
# Using the the sum of numbers we can find what the sum is suppose to be 
# Compare it to what the sum of nums actually is and get the difference