class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        res = 0

        while l < r:
            res = max(res, (min(height[l], height[r]) * (r-l)))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

        # # Brute Force solution:
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         res = max(res, min(height[i], height[j])*(j-i))
        # return res

        # Dynamic programming:
        # dp = {}
        # def dfs(i, j):
        #     if (i, j) in dp:
        #         return dp[(i, j)]
        #     if i >= j or i >= len(height) or j < 0:
        #         return 0
            

        #     dp[(i, j)] = max((min(height[i], height[j])*(j-i)), dfs(i+1, j), dfs(i, j-1))

        #     return dp[(i, j)]
        
        # return dfs(0, len(height)-1)

        # 
    
        