'''
  You are given a sorted unique integer array nums.
  Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
  That is, each element of nums is covered by exactly one of the ranges, 
  and there is no integer x such that x is in one of the ranges but not in nums.
  
  Each range [a,b] in the list should be output as:
    "a->b" if a != b
    "a" if a == b
'''

class Solution:
  def summaryRanges(self, nums: List[int]) -> List[str]:
    if not nums: return nums
    dix = {} 
    dix[nums[0]] = nums[0]
    current = nums[0]
    for i in nums[1:]:
      if dix[current]+1 == i:
        dix[current] = i
      else:
        dix[i] = i 
        current = i 
    result = []
    for i,j in dix.items():
      if i == j:
        result.append(str(i))
      else:
        result.append(str(i) + "->" + str(j))
    return result
#Summary
# 1 Create a dix and for every range the start will be the key and the end will be the val 
# 2 If the val+1 isnt equal to the current num than make a new range
# 3 The iterate through all of the items in the dix and add them to a list in the correct format
 
class Solution:
  def summaryRanges(self, nums: List[int]) -> List[str]:
    result = []
    for num in nums:
      if not result or result[-1][-1]+1 != num:
        result.append([num])
      else:
        result[-1].append(num)
    return [str(i[0]) + "->" + str(i[-1]) if len(i) > 1 else str(i[0]) for i in result]
#Summary 
# Create a list and add new range of list if the last val in the last range != num 
# If result[-1][-1]+1 == num than add num to the list 
# Then use list comprehension to return a list with the right format 