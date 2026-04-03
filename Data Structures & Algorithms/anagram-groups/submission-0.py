class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count={}
        l=[]
        for i, char in enumerate(strs):
            s = "".join(sorted(char))
            if s not in count:
                count[s]=[]
            count[s].append(char)
        for j in count:
            l.append(count[j])
        return l
                    
                

        

        