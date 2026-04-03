class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        l=[]
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        sorted_keys = sorted(count, key=count.get,reverse=True)
        for i in sorted_keys:
            if sorted_keys.index(i)==k:
                break
            else:
                l.append(i)
        return l
                
                
        