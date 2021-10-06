'''Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.'''

class MyQueue: 
  def __init__(self):
    self.newValues = []
    self.oldValues = []
    
  def queue(self, val):
    '''When we add values we add them to the new Stack'''
    self.newValues.append(val)

  def dequeue(self):
    '''When we dequeue we first need to shift the values from the newStack to the oldStack,
      then remove the last values from the oldStack which represents our actual queue.'''
    self.__shiftValues()
    return self.oldValues.pop()
  
  def peek(self):
    ''' To get the last value first shift the values from the newStack to the oldStack.'''
    self.__shiftValues()
    return self.oldValues[-1]

  def __shiftValues(self):
    '''Helper function to move the newStack to the oldStack but only if the oldStack is empty.
    Doing so swaps the values and makes oldStack represent a queue.'''
    if not self.oldValues:
      while self.newValues:
        self.oldValues.append(self.newValues.pop())


if __name__ == '__main__':
  q = MyQueue()
  q.queue(1)
  q.queue(2)
  q.queue(3)
  q.queue(4)
  print(q.newValues)
  print(q.oldValues)
  print(q.peek())
  print(q.newValues)
  print(q.oldValues)
  q.queue(5)
  print(q.newValues)
  print(q.oldValues)
  q.dequeue()
  print(q.newValues)
  print(q.oldValues)
  q.dequeue()
  q.dequeue()
  q.dequeue()
  print(q.newValues)
  print(q.oldValues)
  print(q.peek())
  print(q.newValues)
  print(q.oldValues)