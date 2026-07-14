class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(numCourses)}
        res = []
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        state = [0]*numCourses
        def has_cycle(crs):
            if state[crs]==1:
                return True
            if state[crs]==2:
                return False
            state[crs] = 1
            for pre in adj_list[crs]:
                if has_cycle(pre):
                    return True
            state[crs] = 2
            res.append(crs)
            return False
        for crs in range(numCourses):
            if has_cycle(crs):
                return []
                
        return res