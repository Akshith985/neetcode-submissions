class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
                
       
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                idx = val - 1
                if nums[idx] > 0:
                    nums[idx] = -nums[idx]
                    
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1
                
        
        return n + 1