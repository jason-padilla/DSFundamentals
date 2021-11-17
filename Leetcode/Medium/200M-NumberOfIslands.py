'''
  Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
  An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
  You may assume all four edges of the grid are all surrounded by water.
  Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
  Output: 1 
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      rows, cols = len(grid), len(grid[0])
      def helper(r,c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
          return
        if grid[r][c] == "0":
          return
        if grid[r][c] == "2":
          return 
        if grid[r][c] == "1":
          grid[r][c] = "2"
        helper(r+1,c)
        helper(r-1,c)
        helper(r,c+1)
        helper(r,c-1)
        return 
      count = 0
      for r in range(rows):
        for c in range(cols):
          if grid[r][c] == "1":
            count += 1
            helper(r,c)
      return count