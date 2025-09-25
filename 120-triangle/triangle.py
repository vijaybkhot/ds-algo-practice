class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        # @lru_cache(maxsize=None)
        # def dfs(level, index):
            
        #     if index == len(triangle[level])-1:
        #         if level == n-1:
        #             return triangle[level][index]
        #         else:
        #             return triangle[level][index] + min(dfs(level+1, index), dfs(level+1, index+1))
        #     else:
        #         if level == n-1:
        #             return triangle[level][index]
        #         else:
                    
        #             res = triangle[level][index] + min(dfs(level+1, index), dfs(level+1, index+1))
        #             res = min(res, triangle[level][index+1] + min(dfs(level+1, index+1), dfs(level+1, index+2)))
        #             return res
        
        # return dfs(0, 0)

            
        @lru_cache(None)
        def dfs(level, index):
                # Base case: last row
                if level == n - 1:
                    return triangle[level][index]
                
                # Recursive case: take current value + min of next row choices
                return triangle[level][index] + min(dfs(level+1, index), dfs(level+1, index+1))
            
        return dfs(0, 0)