class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Start = 0
        n = len(cost)
        # cost_0, cost_1 = cost[0], cost[1]
        # i = 0
        # while i < n:
        #     cost_first = cost[i+1] if i+1 < n else 0
        #     cost_second = cost[i+2] if i+2 < n else 0
        #     if cost_first < cost_second:
        #         cost_0 += cost_first
        #         i += 1
        #     else:
        #         cost_0 += cost_second
        #         i += 2
        
        # j = 1
        # while j < len(cost):
        #     cost_first = cost[j+1] if j+1 < n else 0
        #     cost_second = cost[j+2] if j+2 < n else 0
        #     if cost_first < cost_second:
        #         cost_1 += cost_first
        #         j += 1
        #     else:
        #         cost_1 += cost_second
        #         j += 2
            
        # return min(cost_0, cost_1)

        # # recursion - Brute
        # res = sum(cost)
        #         def dfs(i, curr_cost):
        #     nonlocal res
        #     if i >= n:
        #         res = min(res, curr_cost)
        #         return
            
        #     for j in range(1, 3):
        #         new_cost = curr_cost + cost[i]
        #         dfs(i+j, new_cost)
        # dfs(0, 0)
        # dfs(1, 0)
        # return res

        # # Optimized lru cache recursion
        # n = len(cost)

        # @lru_cache(maxsize=None)
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     return cost[i] + min(dfs(i + 1), dfs(i + 2))

        # return min(dfs(0), dfs(1))

        # # Memoization- 
        # n = len(cost)
        # memo = [None]*(n+1)
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     if memo[i] != None:
        #         return memo[i]
        #     memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
        #     return memo[i]
        
        # return min(dfs(0), dfs(1)) 

        # Dynamic programming:
        n = len(cost)
        dp = [0]*(n+1)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[n-1], dp[n-2])

