from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        

        q = deque() # Stores indices
        res = []
        
        for i in range(len(nums)):
            # 1. Remove elements smaller than the current from the back
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            
            # 2. Add current element's index
            q.append(i)
            
            # 3. Remove the front element if it's outside the window
            if q[0] == i - k:
                q.popleft()
            
            # 4. Append the max (front of q) to results if window is full
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res