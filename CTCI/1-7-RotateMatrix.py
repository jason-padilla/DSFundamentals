'''
  Given an image represented b y an NxN matrix, where each pixel in the image is 4bytes,
  write a method to rotate the image by 90 degrees. Can you do this in place?
  [1,2,3]       [7, 4, 1]
  [4,5,6]   ->  [8, 5, 2]
  [7,8,9]       [9, 6, 3]
'''
def rotateMatrix(m:[[int]]) -> [[int]]:
  '''
    Using this method we define a new NxN array filled with 0s.
    As we traverse the original list we add the values to the new list.
    key is result[c][size - 1 - r] = m[r][c]
    swaps the col and rows and starts add into the cols from back to front
    Time: O(N^2) Space: O(N)
  '''
  result = []
  size = len(m)
  for i in range(size):
    temp = [0]*size
    result.append(temp)
  current_col = size
  for r in range(size):
    for c in range(size):
      result[c][size - 1 - r] = m[r][c]
  for i in result:
    print(i)
  return result

def rotateMatrixInPlace(m:[[int]]) -> [[int]]:
  '''
    Does not use an extra array; modifies the same matrix in place
    step1. transpose matrix - swap(array[r][c], array[c][r])
      - diagonals dont get swapped because [0][0] == [0][0] vs [1][2] != [2][1]
    setp2. flip horizontally swap(array[r][c],array[r][n-1-c])
      - swaps values all values except middle values
      step 0       step 1       step 2
      [1, 2, 3]    [1, 4, 7]    [7, 4, 1]
      [4, 5, 6] -> [2, 5, 8] -> [8, 5, 2]
      [7, 8, 9]    [3, 6, 9]    [9, 6, 3]
    Time: O(N^2) Space: O(1)
  '''
  N = len(m)
  #Step 1 
  for r in range(N):
    for c in range(r,N):  # We want to start at every diagonal so we start at r
      temp = m[r][c]
      m[r][c] = m[c][r]
      m[c][r] = temp
  for r in range(N):
    for c in range(N//2):
      temp = m[r][c]
      m[r][c] = m[r][N-1-c]
      m[r][N-1-c] = temp
  for i in m:
    print(i)
  return m
if __name__ == '__main__':
  rotateMatrix([[1,2],[3,4]])
  print()
  rotateMatrix([[1,2,3],[4,5,6],[7,8,9]])
  print()
  rotateMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
  rotateMatrixInPlace([[1,2],[3,4]])
  print()
  rotateMatrixInPlace([[1,2,3],[4,5,6],[7,8,9]])
  print()
  rotateMatrixInPlace([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])