class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m, n = len(word2), len(word1)

        # # Bottom up solution
        # dp = [[0]*(n+1) for _ in range(m+1)]
        # # Base case - increment number of operations to form an empty string
        # for i in range(1, n+1):
        #     dp[0][i] = 1 + dp[0][i-1]

        # # Base case - II - Given an empty string, number of operations required to form any string is equal to the len of the target string - Insert every character one by one
        # for i in range(1, m+1):
        #     dp[i][0] = 1 + dp[i-1][0]
        
        # # Transition:
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         left, top, diag = dp[i][j-1], dp[i-1][j], dp[i-1][j-1]
        #         if word2[i-1] != word1[j-1]:
        #             diag += 1
        #         left += 1
        #         top += 1
        #         dp[i][j] = min(left, top, diag)
        
        # return dp[m][n]


        # Top Down Solution: - Caching and recursion
        dp = {}
        def dfs(i, j):
            if i >= len(word1):
                if j < len(word2):
                    return len(word2) - j
                else:
                    return 0
            if j >= len(word2):
                if i < len(word1):
                    return len(word1) - i
                else:
                    return 1
            if (i, j) in dp:
                return dp[(i, j)]

            left, top, diag = 0, 0, 0
            diag = dfs(i+1, j+1) if word1[i] == word2[j] else 1 + dfs(i+1, j+1)
            left = 1 + dfs(i, j+1)
            top = 1 + dfs(i+1, j)
    
            dp[(i, j)] = min(left, top, diag)

            return dp[(i, j)]
        
        return dfs(0, 0)
            