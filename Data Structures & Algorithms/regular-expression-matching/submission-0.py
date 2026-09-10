class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        
        dp = [False] * (n + 1)
        dp[0] = True
        
        
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[j] = dp[j - 2]
                
        for i in range(1, m + 1):
            prev_diag = dp[0] 
            dp[0] = False   
            
            for j in range(1, n + 1):
                temp = dp[j]
                
                if p[j - 1] == '*':
                    
                    zero_matches = dp[j - 2]
                    
                    char_match = (p[j - 2] == s[i - 1] or p[j - 2] == '.')
                    one_or_more = char_match and temp
                    
                    dp[j] = zero_matches or one_or_more
                else:
                    char_match = (p[j - 1] == s[i - 1] or p[j - 1] == '.')
                    dp[j] = char_match and prev_diag
                    
                prev_diag = temp
                
        return dp[n]