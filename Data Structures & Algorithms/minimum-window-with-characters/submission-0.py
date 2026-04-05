class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d={}
        left=0
        right=0
        formed=0
        v={}
        min_window_str = ""
        for i in t:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for right in range(len(s)):
            
            char = s[right]
            v[char] = v.get(char, 0) + 1
            if char in d and v[char] == d[char]:
                formed += 1
            while formed == len(d):
                current_window = s[left : right + 1]
                if not min_window_str or len(current_window) < len(min_window_str):
                    min_window_str = current_window
                
                char_left = s[left]
                if char_left in d and v[char_left] == d[char_left]:
                    formed -= 1
                    
                v[char_left] -= 1
                left += 1
                

        return min_window_str
        
