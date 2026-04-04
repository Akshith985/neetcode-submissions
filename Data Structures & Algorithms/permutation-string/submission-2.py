class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = collections.Counter(s1)
        window_count = collections.Counter(s2[:len(s1)])
        if s1_count == window_count:
            return True
        for i in range(len(s1),len(s2)):
            new_char=s2[i]
            window_count[new_char]+=1
            old_char=s2[i-len(s1)]
            if window_count[old_char]==1:
                del window_count[old_char]
            else:
                window_count[old_char]-=1
            if window_count==s1_count:
                return True
            
        return False