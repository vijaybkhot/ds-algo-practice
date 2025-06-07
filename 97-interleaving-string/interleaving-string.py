class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # # Solution I : Top-Down DP
        # dp = {}
        # def dfs(i, j, k):
        #     if k == len(s3):
        #         if i == len(s1) and j == len(s2):
        #             return True
        #         else:
        #             return False
            
        #     if (i, j, k) in dp:
        #         return dp[(i, j, k)]
            
        #     is_possible = False
        #     if i < len(s1) and k < len(s3) and s1[i] == s3[k] and dfs(i+1, j, k+1):
        #         is_possible = True
        #     elif j < len(s2) and k < len(s3) and s2[j] == s3[k] and dfs(i, j+1, k+1):
        #         is_possible = True
            
        #     dp[(i, j, k)] = is_possible
        #     return is_possible
        
        # return dfs(0, 0, 0)

        # Solution II - Bottom-up DP:
        if len(s1) + len(s2) != len(s3):
            return False

        # dp[i][j] = True if s3[0:i+j] can be formed by s1[0:i] and s2[0:j]
        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # empty strings can form empty s3

        for i in range(m + 1):
            for j in range(n + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i - 1][j]
                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i][j - 1]

        return dp[m][n]
            
        
        