from collections import deque

class Queue:
  def __init__(self):
    self.queue = deque()
  
  def enqueue(self, val):
    self.queue.appendleft(val)

  def dequeue(self):
    self.queue.pop()

  def front(self):
    return self.queue[-1]

  def is_empty(self) -> bool:
    return len(self.queue) == 0

  def size(self) -> int:
    return len(self.queue)

  def __str__(self):
    result = "Queue(["
    for item in self.queue: 
      result += "'" + str(item) + "', "
    return result[:-2]+"])"

def intToBinary(val) -> str:
  ''' Prints all the numbers from 0 to n inclusive as binary '''
  if val == 0: print(val,"- 0")
  queue = Queue()
  queue.enqueue("1")
  for i in range(val):
    front = queue.front()
    print(i+1,"-",front)
    queue.enqueue(front+"0")
    queue.enqueue(front+"1")
    queue.dequeue()

if __name__ == '__main__':
  #Queue using python list
  qList = [] 
  qList.insert(0,"first arrival")
  qList.insert(0,"second arrival")
  qList.insert(0,"third arrival")
  print(qList)
  qList.pop()
  print(qList)

  #Queue using collections deque
  print("="*40) 
  qDeque = deque()
  qDeque.appendleft("first arrival")
  qDeque.appendleft("second arrival")
  qDeque.appendleft("third arrival")
  print(qDeque)
  qDeque.pop()
  print(qDeque)

  #Queue using Queue Class implementation based off of deque
  print("="*40)
  newQueue = Queue()
  print("Is Empty: ", newQueue.is_empty())
  newQueue.enqueue("first arrival")
  newQueue.enqueue("second arrival")
  newQueue.enqueue("third arrival")
  print(newQueue)
  print("Is Empty: ", newQueue.is_empty())
  print("Size: ", newQueue.size())
  newQueue.dequeue()
  print(newQueue)
  print("Size: ", newQueue.size())

  #Integers to Binary using a Queue
  intToBinary(0)
  print()
  intToBinary(5)
  print()
  intToBinary(10)