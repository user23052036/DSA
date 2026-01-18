# Time complexity: O(V+E)O(V+E)
# Space complexity: O(V+E)O(V+E)

from typing import List

# 1. Cycle Detection (DFS)
class Solution1:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # pre_Map = {i: [] for i in range(numCourses)}  adjacency list
        # { key_expression : value_expression for item in iterable }

        pre_map = {}
        for i in range(numCourses):
            pre_map[i] = []
        
        for course,pre_req in prerequisites:
            pre_map[course].append(pre_req)
        
        # visitSet to find the loop for the current DFS path
        visit_set = set()
        def DFS(course):
            if course in visit_set:
                return False
            if pre_map[course] == []:
                return True
            
            visit_set.add(course)
            for pre_req in pre_map[course]:
                if not DFS(pre_req): return False
            visit_set.remove(course)
            pre_map[course] = []
            return True
        
        # main function to execute (may be that our graph is not connected)
        for course in range(numCourses):
            if not DFS(course): return False
        return True
    
# 2. Topological Sort (Kahn's Algorithm)
