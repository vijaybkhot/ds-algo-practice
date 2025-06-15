class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            if i >= m and j >= n:
                return True
            if j >= n:
                return False


            match = j < n and i < m and (p[j] == '.' or s[i] == p[j])
    
            if j+1 < n and p[j+1] == '*':
                dp[(i, j)] = dfs(i, j+2) or (match and dfs(i+1, j))
                return dp[(i, j)]
            
            if match:
                dp[(i, j)] = dfs(i+1, j+1)
                return dp[(i, j)]

            dp[(i, j)] = False
            return dp[(i, j)]
            
        return dfs(0, 0)