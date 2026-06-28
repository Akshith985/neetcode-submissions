class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        current = []
        
        def backtrack(i):
            # Base Case: If our index reaches the end, we've made a choice 
            # for every number. Save a snapshot copy of our current list!
            if i >= len(nums):
                res.append(current.copy())
                return
                
            # CHOICE 1: Include nums[i] in the current subset
            current.append(nums[i])
            backtrack(i + 1)
            
            # BACKTRACK STEP: Clean up by removing the element 
            # so we can explore the "exclude" path cleanly
            current.pop()
            
            # CHOICE 2: Exclude nums[i] from the current subset
            backtrack(i + 1)
            
        # Kick off the recursion starting at index 0
        backtrack(0)
        return res