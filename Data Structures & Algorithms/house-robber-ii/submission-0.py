from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: If there is only 1 house, just rob it!
        if len(nums) == 1:
            return nums[0]
            
        # Helper function: Standard House Robber I on a linear street
        def rob_linear(houses: List[int]) -> int:
            rob1, rob2 = 0, 0
            for n in houses:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        # Compare skipping the last house vs. skipping the first house
        skip_last = rob_linear(nums[:-1])  # From index 0 to n-2
        skip_first = rob_linear(nums[1:])  # From index 1 to n-1
        
        return max(skip_last, skip_first)