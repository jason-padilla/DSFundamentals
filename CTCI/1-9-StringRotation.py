'''
  Assume you have a mthod isSubstring which checks if one word is a substring of another. 
  Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only 
  one call to isSubstring (e.g "waterbottle" is a rotation of "erbottlewat")
'''
def rotation(s1: str, s2: str) -> bool:
  if len(s1) == len(s2):
    s1 = s1+s1 
    return isSubstring(s1, s2)
  return False

def isSubstring(s1: str, s2: str) -> bool: 
  if len(s2) > len(s1): return False 
  c1, c2 = 0, 0
  count = 0
  while c1 < len(s1) and c2 < len(s2):
    if s1[c1] == s2[c2]:
      c1 += 1
      c2 += 1
    else:
      c1 = c1 - c2 + 1
      c2 = 0
    count += 1
  return c2 == len(s2)
#Summary
#1 We have two pointers that move the same time if the chars equal
#2 If a char isnt equal than c1 resets to the len of c2 and c2 resets to 0
#3 The loop ends when either we reach the end of c1 so we didnt find anything or we reach 
  # the end of c2 which means it is a substring 
#4 If s2 is a substring than c2 will equal s2 len
#5 Time: N+M, Space: Constant
 
def isSubstring2(s1: str, s2: str) -> bool:
  if len(s2) > len(s1): return False 
  for i in range(len(s1)):
    if s1[i] == s2[0]:
      for j in range(len(s2)):
        if i+j >= len(s1) or s1[i+j] != s2[j]:
          break
        if s1[i+j] == s2[j] and j+1 == len(s2):
          return True
  return False
  #Summary 
  #1 We are looping through s1 and if the current char is equal to s2 we start looping through both
  #2 If each char is equal than it will keep looping until the end of s2 is reached; then true will be returned
  #3 If any char isnt equal or we are looping greater than the len of s1 than break and start the search again
  #4 If it isnt found return False
  #5 Time: Squared, Space: Constant
    

if __name__ == '__main__':
  print(rotation("lewaterbott", "waterbottle")) #True
  print(rotation("elwaterbott", "waterbottle")) #False
  print(rotation("carrace", "racecar"))         #True