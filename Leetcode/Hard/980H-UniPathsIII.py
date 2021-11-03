'''
  You are given an m x n integer array grid where grid[i][j] could be:
  1 representing the starting square. There is exactly one starting square.
  2 representing the ending square. There is exactly one ending square.
  0 representing empty squares we can walk over.
  -1 representing obstacles that we cannot walk over.
  Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once. 
  Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
  Output: 2
  Explanation: We have the following two paths: 
  1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
  2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
'''
class Solution:
  def uniquePathsIII(self, grid: List[List[int]]) -> int:
    start = []
    count = 1
    for row in range(len(grid)):
      for col in range(len(grid[0])):
        if grid[row][col] == 1:
          start = [row,col]
        if grid[row][col] == 0:
          count += 1
    return self.dfs(start[0],start[1],grid, [], count)

  def dfs(self,row: int, col: int, grid: List[List[int]], history: [[int,int]], count) -> int:
    if [row,col] in history:
      return 0
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == -1:
      return 0
    elif grid[row][col] == 2:
      if len(history) != count:
        return 0
      return 1
    seen = [i for i in history]
    seen.append([row,col])
    top = self.dfs(row+1, col, grid, seen, count)
    bot = self.dfs(row-1, col, grid, seen, count)
    right = self.dfs(row, col+1, grid, seen, count)
    left = self.dfs(row, col-1, grid, seen, count)
    return top+bot+right+left

#Summary
#Find the starting point, count how many empty spaces there are, keep a track of the visited spaces
#Do a dfs search on every cell from every direction
#If the path reaches the end square than check if the len of the path is equal to the amount of empty cells
#If len(history) == count than return 1 and at the end all the paths will add up to the solution
