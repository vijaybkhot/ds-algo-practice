class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        dp = {}

        def dfs(i, j):
            if i == len(triangle):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            path_sum = 0

            path_sum = (triangle[i][j] + dfs(i+1, j))
            if j+1 < len(triangle[i]):
                path_sum = min(path_sum, (triangle[i][j+1] + dfs(i+1, j+1)))
                
            dp[(i, j)] = path_sum
            return path_sum
        
        return dfs(0, 0)
        