'''
  There are ttrhee typoes of edits that can be performed on strings: insert, remove, or replace a char.
  Given two strings, write a function to check if they are one edit or zero edits away.
  pale -> ple     True
  pales -> pale   True
  pale -> bale    True
  pale -> bake    False
'''
def OneAway(aString:str, bString:str) -> bool:
  if len(aString) == len(bString):
    difference = 0
    for i in range(len(aString)):
      if aString[i] != bString[i]:
        difference += 1
      if difference > 1:
        return False 
    return True
  elif len(aString)+1 == len(bString):
    return diffByOne(aString, bString)
  elif len(aString)-1 == len(bString):
    return diffByOne(bString, aString)
  else:
    return False

def diffByOne(smaller: str, larger: str) -> bool:
  for i in range(len(smaller)):
    if smaller[i] != larger[i]:
      if smaller[i] != larger[i+1]:
        return False 
  return True

if __name__ == '__main__':
  print(OneAway("pale", "ple"))
  print(OneAway("pales", "pale"))
  print(OneAway("pale", "bale"))
  print(OneAway("pale", "bake"))