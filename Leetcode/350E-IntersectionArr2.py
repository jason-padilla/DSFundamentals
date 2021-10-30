'''
  Given two integer arrays nums1 and nums2, return an array of their intersection. 
  Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order. 
  
  Input: nums1 = [1,2,2,1], nums2 = [2,2]
  Output: [2,2]
'''
class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) > len(nums2):
      nums1, nums2 = nums2, nums1
    c = Counter(nums2)
    res = []
    for i in nums1:
      if i in c:
        if c[i] > 0:
          res.append(i)
          c[i] -= 1
    return res

class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:           
    c1 = collections.Counter(nums1)
    c2 = collections.Counter(nums2)
    output = []
    for key in c1.keys() & c2.keys():
      output.extend([key]*min(c1[key], c2[key]))
    return output

class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    c1 = collections.Counter(nums1)
    c2 = collections.Counter(nums2)
    c3 = c1 & c2
    return list(c3.elements())