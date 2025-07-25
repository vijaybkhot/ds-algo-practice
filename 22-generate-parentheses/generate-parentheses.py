class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left, right, path):
            if len(path) == 2*n:
                res.append(path)
                return
            
            if left < n:
                dfs(left+1, right, path+"(")
            
            if right < n and right < left:
                dfs(left, right+1, path+")")
        
        dfs(0, 0, "")
        return res
            
