class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        
        A = [1] + nums + [1]
        n = len(nums)
        
        
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        
        
        for length in range(1, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                
                
                for k in range(i, j + 1):
                    coins = A[i - 1] * A[k] * A[j + 1]
                    dp[i][j] = max(dp[i][j], dp[i][k - 1] + dp[k + 1][j] + coins)
                    
        return dp[1][n]