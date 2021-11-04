'''
  A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
  Each LED represents a zero or one, with the least significant bit on the right.
  For example, the below binary watch reads "4:51".
  Given an integer turnedOn which represents the number of LEDs that are currently on, 
  return all possible times the watch could represent. You may return the answer in any order. 
'''

class Solution:
  def readBinaryWatch(self, turnedOn: int) -> List[str]:
    times = []
    for h in range(12):
      for m in range(60):
        if (bin(h) + bin(m)).count('1') == turnedOn:
          times.append(f'{h}:{m:02d}')
    return times  