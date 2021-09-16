''' 
  Implemewnt an algorithm to determine if a string has all unique chars. 
  What if you cannot use additional data strctures?
'''
def isUnique(aString: str) -> bool:
  ''' 
    Use Dictionary but might be bring the run time when checking if char in Dict 
    Time: O(N) or O(N^2)
  '''
  aDict = {}
  for i in aString:
    if i in aDict:
      return False 
    aDict[i] = 1
  return True

def isUnique0(aString: str) -> bool:
  ''' 
    Use a list
    Time: O(N) or O(N^2)
  '''
  aList = []
  for i in aString:
    for char in aList:
      if char == i:
        return False 
    aList.append(i)
  return True

def isUnique1(aString: str) -> bool:
  ''' 
    Use a Dict but with a try and except to avoid using "in" 
    Time: O(N)
  '''
  aDict = {}
  for i in aString:
    try:
      if aDict[i]:
        return False 
    except:
      aDict[i] = 1
  return True

def isUnique2(aString: str) -> bool:
  ''' 
    Use an array to check index of new chars; uses more space though.
    Assumption that the string is within ASCII not Unicode 
    Time: O(N)
  '''
  unique = [None]*128
  for i in aString:
    converted = ord(i)
    if unique[converted]:
      return False 
    unique[converted] = 1
  return True

if __name__ == '__main__':
  print(isUnique0("abcde"))
  print(isUnique0("unique"))