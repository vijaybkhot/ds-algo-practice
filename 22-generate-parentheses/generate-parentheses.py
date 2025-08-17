class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(l, r , curr_paren):
            if len(curr_paren) == 2*n:
                res.append(curr_paren)
                return
            
            if l < n:
                if l <= r:
                    dfs(l+1, r, curr_paren+'(')
                else:
                    dfs(l+1, r, curr_paren+'(')
                    dfs(l, r+1, curr_paren+')')
            if l == n:
                dfs(l, r+1, curr_paren+')')
        
        dfs(0, 0, "")
    
        return res

            
            