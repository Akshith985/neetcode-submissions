class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)
        farthest = 0
        for i, jump in enumerate(nums):
            if i>farthest:
                return False
            farthest = max(farthest, i+jump)
            if farthest>=target:
                return True
        return True
