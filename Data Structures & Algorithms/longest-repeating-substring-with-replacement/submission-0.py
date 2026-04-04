class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        d={}
        max_f=0
        res=0
        while right<len(s):
            if s[right] in d:
                d[s[right]]+=1
            else:
                d[s[right]]=1
            max_f=max(max_f,d[s[right]])
            out=(right - left + 1)-max_f
            if out>k:
                d[s[left]]-=1
                left+=1
            res=max(res,right-left+1)
            right+=1
        return res
            
        
        