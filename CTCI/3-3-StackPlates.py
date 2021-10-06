'''
  Stack of Plates: Imagine a literal stack of plates. If the stack gets too high, it might topple.
  Therefore, in real likfe, we would likely start a new stack when the previous stack exceeds some 
  threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed
  of several stacks and should create a new stack once the previous one exceeds capacity. 
  SetOfStacks.push() and .pop() should behave identically to a single stack. 
'''

class SetOfStacks():
  def __init__(self, limit):
    self.limit = limit 
    self.stacks = []
    self.current_stack = -1

  def push(self,val):
    '''Add values to a stack, but if that stack is at the limit add a new stack'''
    if len(self.stacks) == 0:
      self._addStack(val)
    elif len(self.stacks[self.current_stack]) == self.limit:
      self._addStack(val)
    else: 
      self.stacks[self.current_stack].append(val)

  def pop(self):
    '''Remove the last value from the current stack, if the current stack is empty remove it'''
    if self.current_stack >= 0:
      self.stacks[self.current_stack].pop() 
      if len(self.stacks[self.current_stack]) == 0:
        self.current_stack -= 1 
        self.stacks.pop() 

  def _addStack(self,val):
    '''Helper function to add a new stack'''
    self.current_stack += 1
    self.stacks.append([val])

if __name__ == '__main__':
  s = SetOfStacks(3)
  s.push(1)
  s.push(2)
  s.push(3)
  print(s.stacks)
  s.pop()
  s.pop()
  s.pop()
  print(s.stacks)
  s.push(1)
  s.push(2)
  s.push(3)
  print(s.stacks)
  s.push(1)
  s.push(2)
  s.push(3)
  print(s.stacks)
