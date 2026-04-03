class Solution:

    def encode(self, strs: List[str]) -> str:
        s1=""
        for s in strs:
            s1+=str(len(s))+"#"+s
        return s1
    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            l=int(s[i:j])
            res.append(s[j+1:j+1+l])
            i=j+1+l
        return res


