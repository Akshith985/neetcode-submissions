from itertools import combinations
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,val1 in enumerate(nums):
            l=[]
            for j,val2 in enumerate(nums):
                if i!=j and val1+val2==target:
                        return [i,j]       
        