'''
  You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
  representing the number of elements in nums1 and nums2 respectively.
  Merge nums1 and nums2 into a single array sorted in non-decreasing order.
  The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
  To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
  and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
  
  Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
  Output: [1,2,2,3,5,6]
  Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
  The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
'''

class Solution:
  def merge(self, nums1, m, nums2, n):
    while m > 0 and n > 0:
      if nums1[m-1] >= nums2[n-1]:
        nums1[m + n - 1] = nums1[m-1]
        m-=1
      else:
        nums1[m + n - 1] = nums2[n-1]
        n-=1
    while n > 0:
      nums1[m+n-1] = nums2[n-1]
      n-=1

#Summary 
#The size of nums1 is m and it is the len of true m + n 
#Instead of replacing from the front and figuring out which is less nums1[m] or nums2[n]
#We should start at the end of nums1[m-1] and add which ever is bigger 
#If it comes to the situation where the values of m bigger than the values of n than 
  #nums2 might be left with some unchecked values 
#Thats why at the end we check that n has also reached the beg if it hasnt
  #than add the remaining values