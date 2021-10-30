'''
  Given two integer arrays nums1 and nums2, return an array of their intersection. 
  Each element in the result must be unique and you may return the result in any order.
  
  Input: nums1 = [1,2,2,1], nums2 = [2,2]
  Output: [2]

  Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
  Output: [9,4]
  Explanation: [4,9] is also accepted.
  #Question worded strange, basically just asking return the values that are in both arrs
'''
class Solution:
  def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    s1, s2 = set(nums1), set(nums2)
    res = []
    for i in s1:
      if i in s2:
        res.append(i)
    return res

class Solution:
  def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    return [i for i in set(nums1) if i in set(nums2)]

class Solution:
  def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))