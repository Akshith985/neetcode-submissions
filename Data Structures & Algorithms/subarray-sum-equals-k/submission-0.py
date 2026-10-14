from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        current_sum = 0
        
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  
        
        for num in nums:
            current_sum += num
            
            
            if current_sum - k in prefix_counts:
                count += prefix_counts[current_sum - k]
                
            
            prefix_counts[current_sum] += 1
            
        return count