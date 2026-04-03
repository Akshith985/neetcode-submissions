class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=0
        for i in nums:
            
            if nums.count(i)>1:
                l+=1
            else:
                continue
        if l>=1:
            return True
        elif l==0:
            return False
                
        
        

                