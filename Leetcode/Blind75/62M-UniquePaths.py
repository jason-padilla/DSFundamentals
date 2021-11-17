'''
  A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
  The robot can only move either down or right at any point in time. 
  The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
  How many possible unique paths are there?
  Input: m = 3, n = 7
  Output: 28
'''
class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    paths = [[1 for c in range(n)] for r in range(m)]
    for r in range(m-2,-1,-1):
      for c in range(n-2,-1,-1):
        paths[r][c] = paths[r+1][c] + paths[r][c+1]
    return paths[0][0]

#Summary
#Make a 2D arr representing the map
#Each cell has a value of 1 because there is atleast 1 path from that cell to the end
#We iterate through the 2D arr backwards and build upon previous paths
#example: last squares there is exactly only 1 way from those cells to the last
#But the top left square will have 2 to go right or go down, this cell builds on the previous cells
#The first cell 0,0 will result in all the possible paths.