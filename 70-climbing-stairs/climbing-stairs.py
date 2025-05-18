class Solution:
    def climbStairs(self, n: int) -> int:

        res = []
        
        @lru_cache(maxsize=None)
        def dfs(total):
            if total == n:
                return 1
            if total > n:
                return 0
            
            return dfs(total + 1) + dfs(total + 2)

        return dfs(0)