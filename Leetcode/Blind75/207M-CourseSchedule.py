'''
  There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
  You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
  For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
  Return true if you can finish all courses. Otherwise, return false.
  Input: numCourses = 2, prerequisites = [[1,0]]
  Output: true
  Explanation: There are a total of 2 courses to take. 
  To take course 1 you should have finished course 0. So it is possible. 
'''
class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    courses = {i: [] for i in range(numCourses)}
    for i in prerequisites:
      courses[i[0]].append(i[1])
    seen = set()
    def helper(course):
      if courses[course] == []:
        return True
      if course in seen:
        return False
      seen.add(course)
      for i in courses[course]:
        res = helper(i)
        if not res: return False
      seen.remove(course)
      courses[course] = []
      return True
    for i in range(numCourses):
      if not helper(i): return False
    return True