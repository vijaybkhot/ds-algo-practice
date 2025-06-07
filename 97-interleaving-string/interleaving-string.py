class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # Solution I : Top-Down DP
        dp = {}
        def dfs(i, j, k):
            if k == len(s3):
                if i == len(s1) and j == len(s2):
                    return True
                else:
                    return False
            
            if (i, j, k) in dp:
                return dp[(i, j, k)]
            
            is_possible = False
            if i < len(s1) and k < len(s3) and s1[i] == s3[k] and dfs(i+1, j, k+1):
                is_possible = True
            elif j < len(s2) and k < len(s3) and s2[j] == s3[k] and dfs(i, j+1, k+1):
                is_possible = True
            
            dp[(i, j, k)] = is_possible
            return is_possible
        
        return dfs(0, 0, 0)

        