class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        #  Top-Down Dynamic Programming
        dp = {}
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            if text1[i] == text2[j]:
                return 1 + dfs(i+1, j+1)
            lcs = max(dfs(i+1, j), dfs(i, j+1))
            dp[(i, j)] = lcs
            return lcs
        
        return dfs(0, 0)
        # # Recursion -
        # def dfs(i, j):
        #     if i == len(text1) or j == len(text2):
        #         return 0
        #     if text1[i] == text2[j]:
        #         return 1 + dfs(i+1, j+1)
        #     return max(dfs(i+1, j), dfs(i, j+1))
        
        # return dfs(0, 0)

        # # Bottom-up Dynamic programming
        # dp = [[0]*(len(text1)+1) for _ in range(len(text2)+1)]
        # for i in range(1, len(text2)+1):
        #     for j in range(1, len(text1)+1):
        #         if text1[j-1] == text2[i-1]:
        #             dp[i][j] = dp[i-1][j-1] + 1
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # return dp[-1][-1]
