class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        # return True     # The answer is alway true
        # # Top-down DP
        # dp = {}
        # def dfs(i, j):
        #     if i > j:
        #         return 0
        #     if (i, j) in dp:
        #         return dp[(i, j)]

        #     left = piles[i] - dfs(i+1, j)
        #     right = piles[j] - dfs(i, j-1)
            
        #     dp[(i, j)] = max(left, right)
        #     return dp[(i, j)]


        # return dfs(0, len(piles)-1) > 0

        #  Bottom-up DP
        n = len(piles)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    dp[i][j] = piles[i]
        
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1  
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])

        return dp[0][n-1] > 0