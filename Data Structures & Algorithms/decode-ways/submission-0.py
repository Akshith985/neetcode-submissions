class Solution:
    def numDecodings(self, s: str) -> int:
        # Base case: empty string or starts with invalid '0'
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        # dp[i] stores the number of valid ways to decode prefix of length i
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # Base multiplier for empty string
        dp[1] = 1  # Since s[0] != '0', there's 1 way to decode length 1
        
        for i in range(2, n + 1):
            # Option 1: Consider single digit s[i-1]
            one_digit = int(s[i - 1:i])
            if 1 <= one_digit <= 9:
                dp[i] += dp[i - 1]
                
            # Option 2: Consider two digits s[i-2:i]
            two_digits = int(s[i - 2:i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]
                
        return dp[n]