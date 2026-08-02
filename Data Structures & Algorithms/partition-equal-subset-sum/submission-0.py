class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        
        
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        
        
        dp = {0}
        
        for num in nums:
            
            next_dp = set(dp)
            for current_sum in dp:
                new_sum = current_sum + num
                if new_sum == target:
                    return True
                if new_sum < target:
                    next_dp.add(new_sum)
            dp = next_dp
            
        return target in dp