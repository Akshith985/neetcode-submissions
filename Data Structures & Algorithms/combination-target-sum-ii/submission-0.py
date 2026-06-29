class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        current = []
        def backtrack(i, current_target):
            if current_target == 0:
                res.append(current.copy())
                return
            if current_target < 0:
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                current.append(candidates[j])
                backtrack(j+1,current_target-candidates[j])
                current.pop()
        backtrack(0,target)
        return res