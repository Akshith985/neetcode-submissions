class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        max_len = max(len(w) for w in wordDict) if wordDict else 0
        
        n = len(s)
        # dp[i] means s[:i] can be segmented into dictionary words
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string
        
        for i in range(1, n + 1):
            
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  
                    
        return dp[n]