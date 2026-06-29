class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        current = []
        def backtrack(i, current_target):
            if current_target==0:
                res.append(current.copy())
                return
            if current_target<0 or i >= len(nums):
                return
            current.append(nums[i])
            backtrack(i,current_target-nums[i])
            current.pop()
            backtrack(i+1,current_target)
        backtrack(0,target)
        return res
