class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # MOD = 10**9 + 7
        
        # # Precompute powers to avoid repeated i**x
        # powers = []
        # i = 1
        # while i**x <= n:
        #     powers.append(i**x)
        #     i += 1
        
        # from functools import lru_cache
        
        # @lru_cache(None)
        # def dfs(index, total):
        #     if total == n:
        #         return 1
        #     if total > n or index >= len(powers):
        #         return 0
            
        #     # Include current power OR skip it
        #     return (dfs(index + 1, total + powers[index]) + 
        #             dfs(index + 1, total)) % MOD
        
        # return dfs(0, 0)

        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            val = i**x
            if val > n:
                break
            for j in range(n, val - 1, -1):
                dp[j] = (dp[j] + dp[j - val]) % MOD

        return dp[n]