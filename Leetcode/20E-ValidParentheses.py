'''
  Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
  An input string is valid if:
  Open brackets must be closed by the same type of brackets.
  Open brackets must be closed in the correct order.

'''
class Solution:
  def isValid(self, s: str) -> bool:
    if len(s) % 2 != 0: return False
    dix = {'(':')', '{':'}', '[':']'}
    st = []
    for i in s:
      if i == '(' or i == '{' or i == '[':
        st.append(i)
      elif len(st) == 0 or dix[st[-1]] != i:
        return False 
      else:
        st.pop()
    return len(st) == 0