class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i ^ num
        return res