''' 
  Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
  The relative order of the elements should be kept the same.
  Since it is impossible to change the length of the array in some languages, 
  you must instead have the result be placed in the first part of the array nums. 
  More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
  It does not matter what you leave beyond the first k elements.
  Return k after placing the final result in the first k slots of nums.
  Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    idx = 0
    for i in nums:
      if i != nums[idx]:
        idx += 1
        nums[idx] = i 
    return idx+1

#Summary 
#1 Since they are in order we only need to check if the current correct place
  #is equal to the current val 
#2 If its not than we increase the idx and add it to that place 
#3 If it is equal than we just skip it and move on 
#4 Return the count of the unqiue vals