'''
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''
class Solution:
  def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    l, r = 0, n
    while l < r:
      mid = (l+r)//2      
      if isBadVersion(mid):
        r = mid
      else:
        l = mid + 1
    return l
#Summary 
#To find the first bad version we need to move inward 
#If the mid point is bad than we make right be the mid
  # This means that any val after is also bad  
#If the mid isnt bad that we make left = mid+1
  # This means that none of the left side from right is bad
# We keep narrowing down until we find the first bad