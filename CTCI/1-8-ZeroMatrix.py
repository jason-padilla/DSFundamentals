'''
  Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
  You must do it in place.
'''

class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = set()
    cols = set()
    m = len(matrix)
    n = len(matrix[0])
    for r in range(m):
      for c in range(n):
        if matrix[r][c] == 0:
          rows.add(r)
          cols.add(c)
    for r in range(m):
      for c in range(n):
        if r in rows:
          matrix[r][c] = 0
        if c in cols:
          matrix[r][c] = 0
#Summary 
#1 You iterate through all of the values and mark the rows and cols that will have zeros
#2 Iterate through all of the values again and if the row/col the value is on is marked change it to zero
#3 Time: Quadratic, Space: Linear

class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])
    zeroRow = False
    
    #Mark all of top and left 0s
    for r in range(m):
      for c in range(n):
        if matrix[r][c] == 0:
          matrix[0][c] = 0
          if r > 0:
            matrix[r][0] = 0
          else:
            zeroRow = True
            
    #Change inner values to 0
    for r in range(1,m):
      for c in range(1,n):
        if matrix[0][c] == 0 or matrix[r][0] == 0:
          matrix[r][c] = 0
          
    #Change 0idx of every row
    if matrix[0][0] == 0:
      for r in range(1,m):
        matrix[r][0] = 0
        
    #Change every elm of row 0
    if zeroRow:
      for c in range(n):
        matrix[0][c] = 0

#Summary 
#1 Iterate through all of the values and mark all the rows and cols that will need 0s
  #Except the current row is 0; we will instead make a marker that it the first row must be zeroed 
  #We do this to prevent all of the values changing to 0
#2 Then we change all of the inner values and check if the current row/col they are on is marked as a 0 row/col
#3 Then we check if matrix[0][0] == 0, if it is that means that a value in col 0 had a 0 so now they must all be 0
#4 Last we check if the zeroRow needs to be zeroed; if it is its because their was an initial 0 in row 0