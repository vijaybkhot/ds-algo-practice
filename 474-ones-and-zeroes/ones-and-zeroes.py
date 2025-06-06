class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        # # Recursive approach
        # self.res = 0
        # def dfs(i, curr_str, count):
        #     zeroes = curr_str.count('0')
        #     ones = curr_str.count('1')
        #     if zeroes <= m and ones <= n:
        #         self.res = max(self.res, count)
            
        #     if i == len(strs):
        #         return
        #     dfs(i+1, curr_str+strs[i], count+1)
        #     dfs(i+1, curr_str, count)
        
        # dfs(0, "", 0)
        # return self.res
        
        # Top-down memoization approach
        dp = {}

        def dfs(i, m, n):
            if i == len(strs):
                return 0

            if (i, m, n) in dp:
                return dp[(i, m, n)]

            zeroes = strs[i].count('0')
            ones = strs[i].count('1')
            not_take = dfs(i+1, m, n)
            take = 0
            
            if zeroes <= m and ones <= n:
                take = 1+ dfs(i+1, m-zeroes, n-ones)
            
            dp[(i, m, n)] = max(take, not_take)
            return dp[(i, m, n)]
            
            
            
        return dfs(0, m, n)
            
        