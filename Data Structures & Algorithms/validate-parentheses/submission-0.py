class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        l=[]
        formed=0
        for char in s:
            if char in mapping:
                if not l:
                    return False
                top=l.pop()
                if mapping[char]!=top:
                    return False
                    break
            else:
                l.append(char)
        return not l
            

        