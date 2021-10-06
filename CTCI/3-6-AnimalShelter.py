from collections import deque
'''
  Animal Shelter; An animal shelter, which holds only dogs and cats, operates on a strictly 
  "first in, first out" basis. People must adopt either the oldest of all the animals at the shelter 
  or they must either select a dog or cat and receive the oldest animal of that type. 
  They cannot select which specific animal they would like. Create a data structure to 
  maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, dequeueCat.
'''
class AnimalShelter():
  def __init__(self):
    self.all = deque()
    self.dogs = deque()
    self.cats = deque()
  
  def enqueue(self, animal):
    self.all.appendleft(animal)
    if animal[1] == "dog":
      self.dogs.appendleft(animal)
    else:
      self.cats.appendleft(animal)

  def dequeueAny(self):
    '''Remove from the queue but balance it first to make sure the right value is being removed'''
    self.__balance()
    animal = self.all.pop()
    if animal[1] == "dog":
      self.dogs.pop()
    else:
      self.cats.pop()

  def dequeueDog(self):
    self.dogs.pop()

  def dequeueCat(self):
    self.cats.pop()
  
  def peek(self):
    self.__balance()
    return self.all[-1] 

  def __balance(self):
    ''' A helper function that balances all of the queues. When an specific type of animal 
    is dequeued the all queue is not updated. We do so by removing any values from the all queue
    until it equals the top value in either the dog queue or the cat queue'''
    if not self.cats: 
      while self.all[-1] != self.dogs[-1]:
        self.all.pop()
    elif not self.dogs():
      while self.all[-1] != self.cats[-1]:
        self.all.pop()
    else:
      while self.all[-1] != self.cats[-1] and self.all[-1] != self.dogs[-1]:
        self.all.pop()

  def showShelter(self):
    print("All:", self.all)
    print("Dogs:", self.dogs)
    print("Cats:", self.cats)
    print("===================")

if __name__ == '__main__':
  a = AnimalShelter()
  a.enqueue(["Jorgy", "dog"])
  a.enqueue(["Kitty", "cat"])
  a.enqueue(["Rufus", "dog"])
  a.enqueue(["Mittens", "cat"])
  a.enqueue(["Wolf", "dog"])
  a.showShelter()
  a.dequeueCat()
  a.showShelter()
  a.dequeueCat()
  a.showShelter()
  a.dequeueAny()
  a.showShelter()
