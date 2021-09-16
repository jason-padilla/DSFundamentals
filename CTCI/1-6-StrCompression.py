def compress(aString: str) -> str:
  '''
    Uses string concatination but string concatenation's time complexity is O(N)
    Why? because strings are immutable and the only they are modified is to copy them into a new one
    Time: O(N^2) 
  '''
  newString = ""
  count = 1
  for i in range(1,len(aString)):
    if aString[i] != aString[i-1]:
      newString += aString[i-1]
      newString += str(count)
      count = 1
    else:
      count +=1
  newString += aString[i-1]
  newString += str(count)
  return newString if len(newString) < len(aString) else aString

def compress(aString: str) -> str:
  '''
    Instead of using string concatenation use a list to add the new values to the list.
    Then use .join to make all the strings inside of a list into 1 string
    Time: O(N) 
  '''
  new = []
  newString = ""
  count = 1
  for i in range(1,len(aString)):
    if aString[i] != aString[i-1] or i == len(aString)-1:
      new.append(aString[i-1])
      new.append(str(count))
      count = 1
    else:
      count +=1
  new = ''.join(new)
  return new if len(new) < len(aString) else aString

if __name__ == '__main__':
  print(compress("aabcccccaaa"))
  print(compress("abc"))