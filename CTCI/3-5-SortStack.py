''' 
  Sort Stack: Write a program to sort a stack such that the smallest items are on the top, 
  You can use an additional temporary stack, but you may not copy the elements into another 
  data strcuture like an array. The stack supports the following operations: push, pop, peek. 
''' 

class SortedStack():
  '''A stack that every time you add a new value it sorts the values inside 
    and makes the top value the smallest value.'''
  def __init__(self):
    self.stack = []
  
  def push(self, word):
    '''Push values to the stack if the new value is less than the top value.
      If its not pop the values and put them into temp stack and then add value.
      Lastly move all the values from the temp stack back to the main stack.'''
    if not self.stack: 
      self.stack.append(word)
    elif self.peek() >= word:
      self.stack.append(word)
    else:
      temp = [] 
      while self.stack and self.stack[-1] < word:
        temp.append(self.stack.pop())
      self.stack.append(word)
      while temp:
        self.stack.append(temp.pop())

  def pop(self):
    '''Remove the top value in the stack and return it'''
    if self.stack: 
      return self.stack[-1] 

  def peek(self):
    '''Return the top value in the stack'''
    if self.stack:
      return self.stack[-1]

def sortStack(s:list):
  '''A function that takes a stack and sorts it by moving values into a temp stack.
    If the top value in the stack is greater than the top value in the temp stack,
    than move the top value into a temp val and then remove all the values from the 
    temp stack and put them back into the mainStack. At the end move all the values 
    from the tempStack and move them back to the mainStack.
  '''
  sortedTemp = [] 
  while s:
    if not sortedTemp:
      sortedTemp.append(s.pop()) 
    elif s[-1] <= sortedTemp[-1]:
      sortedTemp.append(s.pop())
    else: 
      temp = s.pop()
      while sortedTemp and temp > sortedTemp[-1]:
        s.append(sortedTemp.pop())
      sortedTemp.append(temp)
  while sortedTemp: 
    s.append(sortedTemp.pop())

if __name__ == '__main__':
  s = SortedStack()
  s.push(2)
  print(s.stack)
  s.push(3)
  print(s.stack)
  s.push(4)
  print(s.stack)
  s.push(5)
  print(s.stack)
  s.push(1)
  print(s.stack)
  print(s.peek())
  us = [1,5,67,3,8,9]
  sortStack(us)
  print(us)
