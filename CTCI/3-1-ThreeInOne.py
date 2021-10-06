from collections import deque, Counter
''' 
  Three In One: Describe how you could use a single array to implement three stacks.
''' 

class MultiStack():
  def __init__(self):
    self.sizePerStack = 9
    self.numOfStacks = 3
    self.main = [None]*(self.sizePerStack * self.numOfStacks)
    self.sizes = [-1,-1,-1]

  def push(self, stackNum, value):
    ''' 
      Push to a specific stack but only if its within range and if its not full.
      The position it will go into is decided by the stackNum*sizePerStack and 
      how many values are already inside that current stack.
    '''
    if stackNum < self.numOfStacks:
      if not self._isStackFull(stackNum):
        self.sizes[stackNum] += 1
        position = (self.sizePerStack * stackNum) + self.sizes[stackNum]
        self.main[position] = value
  
  def peek(self, stackNum):
    '''Show the last value of the specified stack'''
    if stackNum < self.numOfStacks:
      if self.sizes[stackNum] != -1:
        position = (self.sizePerStack * stackNum) + self.sizes[stackNum]
        return self.main[position]

  def pop(self, stackNum):
    '''Remove the last value of the specified stack and return it'''
    if stackNum < self.numOfStacks:
      if self.sizes[stackNum] != -1:
        position = (self.sizePerStack * stackNum) + self.sizes[stackNum]
        result = self.main[position]
        self.main[position] = None 
        self.sizes[stackNum] -= 1
        return result

  def _isStackFull(self, stackNum):
    '''Helper function to check if the specified stack is full'''
    if self.sizes[stackNum] < self.sizePerStack:
      return False 
    return True

if __name__ == '__main__':
  three = MultiStack()
  three.push(0,1)
  three.push(1,10)
  three.push(2,22)
  print(three.main)
  print(three.pop(2))
  print(three.main)