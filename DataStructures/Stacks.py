from collections import deque

'''
  Python lists and deques are similar however deque's use of memory is more like an actual stack compared to lists.
  listStack = []   deqeueStack = deque()
'''

class Stack: 
  '''Traditional Stack Implementation Using Deqeue'''
  def __init__(self):
    self.stack = deque() 
  
  def push(self,val):
    self.stack.append(val)
  
  def pop(self):
    self.stack.pop() 
  
  def peek(self):
    return self.stack[-1]
  
  def is_empty(self):
    return len(self.stack) == 0 
  
  def size(self):
    return len(self.stack)
  
  def print(self):
    print(self.stack)

def reverseStringList(newStr: str) -> str:
  ''' Reverse a given string using a python list as a stack '''
  result = "" 
  stack = []
  for char in newStr:
    stack.append(char)
  while stack: 
    result += stack.pop()
  return result

def reverseString(newStr: str) -> str:
  ''' Reverse a given string using a the created Stack class inherited from deque ''' 
  result = ""
  strStack = Stack()
  for char in newStr:
    strStack.push(char)
  while not strStack.is_empty():
    result += strStack.peek()
    strStack.pop()
  return result

def is_valid(statement: str) -> bool: 
  ''' Given a statement with parantheses determine if the statement is valid '''
  table = {"(":")","{":"}","[":"]"}
  stack = Stack()
  for char in statement:
    if char in table.keys():
      stack.push(char)
    elif char in table.values():
      if stack.is_empty(): return False 
      if table[stack.peek()] != char: return False 
      stack.pop()
  return True

if __name__ == '__main__':
  #Stack using python list
  print("="*40)
  listStack = [] 
  listStack.append("first push")
  listStack.append("second push")
  listStack.append("second push")
  print(listStack)
  listStack.pop()
  print(listStack)

  #Stack using deque
  print("="*40)
  stack = deque()
  stack.append("first append")
  stack.append("second append")
  stack.append("third append")
  print(stack)
  stack.pop() 
  print(stack)

  #Stack using Stack class implementation based off of deque
  print("="*40)
  newStack = Stack() 
  print("Is Empty: ", newStack.is_empty())
  newStack.push("first")
  newStack.push("second")
  print("Is Empty: ", newStack.is_empty())
  newStack.print()
  print("Peek: ", newStack.peek())
  print("Size: ", newStack.size())
  newStack.pop() 
  newStack.print()
  print("Size: ", newStack.size())

  #Reverse a String using Stack List and Stack Class
  print("="*40)
  word = "Hello"
  print(word)
  print(reverseStringList(word))
  word = "World"
  print(word)
  print(reverseString(word))
  
  #Check if the parentheses in a string statement are valid
  print("="*40)
  print(is_valid("({a+b})")) # True
  print(is_valid("))((a+b}{"))  #False
  print(is_valid("((a+b))")) #True
  print(is_valid("((a+g))")) #True
  print(is_valid("))")) #False
  print(is_valid("[a+b]*(x+2y)*{gg+kk}")) #True