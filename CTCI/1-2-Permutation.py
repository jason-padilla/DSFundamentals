''' 
  Given a two strings, write a method to decide if one is a permutation of the other 
  Permuation: two strings with the same characters but in a different order
'''

def check_permutation(aWord:str, bWord: str) -> bool:
  '''
    Check permutation using sort() 
    Time: O(n log n)
  '''
  if len(aWord) != len(bWord): return False 
  return sorted(aWord) == sorted(bWord)

def check_permutation0(aWord:str, bWord: str) -> bool:
  '''
    Use a dict to keep count of the characters; uses the 'in' operator
    Time: O(n) or O(n^2) 
  '''
  aDict = {} 
  for i in aWord:
    if i in aDict:
      aDict[i] += 1
    aDict[i] = 1
  for j in bWord:
    if j not in aDict: 
      return False 
    aDict[j] -= 1
    if aDict[j] < 0:
      return False
  return True

if __name__ == '__main__':
  print(check_permutation("dog", "god"))
  print(check_permutation("apple", "abble"))
  print(check_permutation0("dog", "god"))
  print(check_permutation0("apple", "abble"))