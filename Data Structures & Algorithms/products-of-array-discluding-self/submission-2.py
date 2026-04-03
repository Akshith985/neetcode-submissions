import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m=[]
        for idx in range(len(nums)):
            output = nums[:idx] + nums[idx+1:] 
            m.append(math.prod(output))
        return m
  
