'''
  118E
  Given an integer numRows, return the first numRows of Pascal's triangle.
  In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

  Input: numRows = 5                                    Input: numRows = 1
  Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]     Output: [[1]] 

  119E 
  Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
  In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
  
  Input: rowIndex = 3     Input: rowIndex = 0
  Output: [1,3,3,1]       Output: [1]
'''

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    triangle = [[1]]
    for i in range(1,numRows):
        temp = [0]+triangle[-1]+[0]
        row=[]
        for elm in range(len(temp)-1):
            row.append(temp[elm]+temp[elm+1])
        triangle.append(row)
    return triangle

class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    triangle = [[1]]
    for i in range(1,rowIndex+1):
        temp = [0]+triangle[-1]+[0]
        row=[]
        for elm in range(len(temp)-1):
            row.append(temp[elm]+temp[elm+1])
        triangle.append(row)
    return triangle[-1]

#SUMMARY 
#Both questions are essential the same other than 119E starts at 0 index and returns the target row
  #VS 118 returning the entire triangle
#1 The trick to coding Pascals triangle is adding 0s at the end of each previous row
#2 We initialize our result triangle to the first row in the triangle [[1]]
#3 After we will iterate from 1 to range(numRows) and build each row 
#4 First we build a temp row with the [0]+prev_row+[0] = [....]
#5 Then we iterate over the range of elms in temp - 1 and add pairs temp[elm]+temp[elm+1]
#6 This will build our individual row and then finally add it to the triangle