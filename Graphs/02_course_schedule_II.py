from typing import List

# Cycle Detection (DFS)
class Solution1:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # created an adjacency matrix for all the nodes
        adj_matrix = {i: [] for i in range(numCourses)}

        # fill adj_matrix data
        for cource,pre_req in prerequisites:
            adj_matrix[cource].append(pre_req)
        
        output = []
        visited,cycle = set(), set() 
        def DFS(course):
            if course in cycle: #cycle detected
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for pre_req in adj_matrix[course]:
                if not DFS(pre_req): return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        # graph may be disjoing loop through all nodes and call DFS for each
        for course in range(numCourses):
            if not DFS(course): return []
        return output


# Topological Sort (Kahn's Algorithm)





# Topological Sort (DFS)