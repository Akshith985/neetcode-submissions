class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
            
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        
        
        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
                
       
        count1, count2 = 0, 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
                
        result = []
        threshold = len(nums) // 3
        
        if cand1 is not None and count1 > threshold:
            result.append(cand1)
        if cand2 is not None and cand2 != cand1 and count2 > threshold:
            result.append(cand2)
            
        return result