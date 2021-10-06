''' 
  Stack Min: How would you design a stack which, in addition to push and pop, has a function 
  min which returns the minimum element? Push, pop and min should all operate in O(1) time 
''' 

class StackWithMin():
  def __init__(self):
    self.minStack = []
    self.main = []
  
  def push(self, val):
    '''Push to the main stack but if val is less than current minStack add to it'''
    if len(self.minStack) == 0:
      self.minStack.append(val)
    elif self.minStack[-1] > val:
      self.minStack.append(val) 
    self.main.append(val)
  
  def pop(self):
    '''If the current minStack is equal to the last value pop it and pop from main'''
    if self.minStack[-1] == self.peek():
      self.minStack.pop()
    self.main.pop() 

  def peek(self):
    '''Return the last value'''
    return self.main[-1]

  def min(self):
    '''Return minimum value, which is at the top of the minStack'''
    if len(self.minStack) != 0:
      return self.minStack[-1]

if __name__ == '__main__':
  s = StackWithMin()
  print("Nothing: ", s.min())
  s.push(5)
  print(s.min())
  s.push(6)
  print(s.min())
  s.push(3)
  print(s.min())
  s.push(7)
  print(s.min())
  s.pop()
  print(s.min())
  s.pop()
  print(s.min())