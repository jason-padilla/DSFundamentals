'''
  Implement a first in first out (FIFO) queue using only two stacks. 
  The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
  Implement the MyQueue class:
  void push(int x) Pushes element x to the back of the queue.
  int pop() Removes the element from the front of the queue and returns it.
  int peek() Returns the element at the front of the queue.
  boolean empty() Returns true if the queue is empty, false otherwise.
'''
class MyQueue:
  def __init__(self):
    self.new = []
    self.old = []

  def push(self, x: int) -> None:
    self.new.append(x)

  def pop(self) -> int:
    if not self.old:
      while self.new:
        self.old.append(self.new.pop())
    return self.old.pop()

  def peek(self) -> int:
    if not self.old:
      while self.new:
        self.old.append(self.new.pop())
    return self.old[-1]

  def empty(self) -> bool:
    return (len(self.new) + len(self.old)) == 0