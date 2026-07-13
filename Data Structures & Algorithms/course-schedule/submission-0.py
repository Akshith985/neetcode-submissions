from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build an Adjacency List to map: course -> list of its prerequisites
        adj_list = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
            
        # 2. Track states: 0 = unvisited, 1 = visiting, 2 = visited/cleared
        state = [0] * numCourses
        
        def has_cycle(crs):
            # If we hit a node we are currently visiting, a cycle exists!
            if state[crs] == 1:
                return True
            # If we hit a node already fully cleared, no need to check it again
            if state[crs] == 2:
                return False
                
            # Commit: Mark the course as currently 'visiting'
            state[crs] = 1
            
            # Recursively check all prerequisites for this course
            for pre in adj_list[crs]:
                if has_cycle(pre):
                    return True
                    
            # Backtrack/Clear: Mark the course as fully 'visited' and safe
            state[crs] = 2
            return False

        # 3. Check every single course (handles disconnected graphs)
        for crs in range(numCourses):
            if has_cycle(crs):
                return False # Paradox found! Cannot finish all courses.
                
        return True