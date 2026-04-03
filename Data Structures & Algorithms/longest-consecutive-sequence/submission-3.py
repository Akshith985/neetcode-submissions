class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l=[]
        k=[]
        if len(nums)>0:
            for i in nums:
                if (i-1) not in nums:
                    current_num=i
                    seq=[]
                    while current_num in nums:
                        seq.append(current_num)
                        current_num+=1
                    l.append(seq)
            for n in l:
                k.append(len(n))
            v=sorted(k)
            return v[-1]  
        else:
            return 0          