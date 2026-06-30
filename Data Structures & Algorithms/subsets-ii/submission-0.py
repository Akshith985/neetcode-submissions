class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        current = []
        
        def backtrack(i):
            # Base Case: If we've made a choice for every element, save the snapshot
            if i >= len(nums):
                res.append(current.copy())
                return
                
            # --- CHOICE 1: INCLUDE nums[i] ---
            current.append(nums[i])
            backtrack(i + 1)
            current.pop() # Clean up the choice
            
            # --- CHOICE 2: EXCLUDE nums[i] AND SKIP ALL ITS DUPLICATES ---
            # Instead of just moving to i + 1, we advance the pointer past
            # any elements that are identical to the one we just rejected.
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
                
            # Move to the next completely unique number
            backtrack(i + 1)
            
        # Kick off the decision tree at index 0
        backtrack(0)
        return res