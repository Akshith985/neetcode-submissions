class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        seen={}
        max_v=0
        for right in range(len(s)):
            char=s[right]
            if char in seen and seen[char]>=left:
                left=seen[char]+1
            seen[char]=right
            max_v = max(max_v, right - left + 1)
        return max_v