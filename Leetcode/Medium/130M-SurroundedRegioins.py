'''
  Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
  A region is captured by flipping all 'O's into 'X's in that surrounded region.
  ['X', 'X', 'X', 'X']      ['X', 'X', 'X', 'X']      ['X', 'X', 'X', 'X']
  ['X', 'O', 'O', 'X']  ->  ['X', 'O', 'O', 'X']  ->  ['X', 'X', 'X', 'X']
  ['X', 'X', 'O', 'X']      ['X', 'X', 'O', 'X']      ['X', 'X', 'X', 'X']
  ['X', 'O', 'X', 'X']      ['X', 'T', 'X', 'X']      ['X', 'O', 'X', 'X']
'''

class Solution:
  def solve(self, board: List[List[str]]) -> None:
    rows, cols = len(board), len(board[0])
    #Step 2: Change edge 0s and surroudings to Ts
    def capture(r,c):
      if (0 <= r < rows) and (0 <= c < cols) and board[r][c] == 'O': 
        board[r][c] = 'T'
        capture(r+1,c)
        capture(r-1,c)
        capture(r,c+1)
        capture(r,c-1)
      return 
    #Step 1: Find all edge Os
    for r in range(rows):
      for c in range(cols):
        if board[r][c] == 'O' and (r in [0,rows-1] or c in [0,cols-1]):
          capture(r,c)
    #Step 3: Change non Ts to Xs
    for r in range(rows):
      for c in range(cols):
        if board[r][c] == 'O':
          board[r][c] = 'X'
    #Step 4: Revert all Ts to Os
    for r in range(rows):
      for c in range(cols):
        if board[r][c] == 'T':
          board[r][c] = 'O'
#Summary:
#The key is in the fact that any O that is at the edge cant change to X because 1 of there sides isnt an X
#Also if any of those edge Os is surrounded by other Os that are not edges they also cant be Xs
#So change all of the edge Os and its surroundings into Ts
#Then we change all non Ts that are Os into Xs
#Finally change all Ts back to Os