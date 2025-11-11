class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
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