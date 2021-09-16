''' 
  Given a string write a function to check if it is a permutation of a palindrome. 
  Palindrome: a word or phrase that is the same forwards and backwards.
  Permutation: a rearrangment of letters.
  Input: Tact Coa 
  Ouput: True (permuations: "taco cat")
'''

def isPaliPerm(phrase: str) -> bool:
  '''
    Uses a dict; may lower runtime due to for "in" method
    Uses a < i < z comparison 
  ''' 
  aDict = {}
  phrase = phrase.lower()
  for i in phrase:
    if 'a' <= i and i <= 'z':
      if i not in aDict:
        aDict[i] = 1
      else:
        aDict[i] += 1
  singles = 0
  for i in aDict.values():
    singles += i % 2
  return singles <= 1

def isPaliPerm0(phrase: str) -> bool: 
  '''
    Uses a list of size 128 to represent all ASCII values 
    Uses a < i < z comparison 
  ''' 
  aList = [0]*128
  phrase = phrase.lower()
  for i in phrase:
    if 'a' <= i and i <= 'z':
      aList[ord(i)] += 1
  singles = 0
  for i in aList:
    singles += i % 2
  return singles <= 1

if __name__ == '__main__':
  print(isPaliPerm("taco cat"))
  print(isPaliPerm("Tact Coa"))
  print(isPaliPerm("ra p"))
  print(isPaliPerm0("taco cat"))
  print(isPaliPerm0("Tact Coa"))
  print(isPaliPerm0("ra p"))