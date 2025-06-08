class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        dp = {}
        def dfs(i, M, alice):
            if i >= len(piles):
                return 0
            if (i, M, alice) in dp:
                return dp[(i, M, alice)]
            if alice:
                total = 0
                for k in range(1, 2*M+1):
                    total = max(total, (sum(piles[i:i+k]) + dfs(i+k, max(M, k), False)))
            else:
                total = float('inf')
                for k in range(1, 2*M+1):
                    total = min(total, (dfs(i+k, max(M, k), True)))

            
            dp[(i, M, alice)] = total
            return total
        
        return dfs(0, 1, True)
            