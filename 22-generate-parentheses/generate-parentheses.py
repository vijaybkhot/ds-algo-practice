class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open_paren, closed_paren, path):
            if len(path) == 2*n:
                
                res.append(''.join(path[:]))
                return
        

            if open_paren == n:
                path.append('(')
                dfs(open_paren-1, closed_paren, path)
                path.pop()
            
            elif open_paren == 0:
                path.append(')')
                dfs(open_paren, closed_paren-1, path)
                path.pop()

            elif (open_paren <= closed_paren) and (open_paren > 0):
                path.append('(')
                dfs(open_paren-1, closed_paren, path)
                path.pop()

                path.append(')')
                dfs(open_paren, closed_paren-1, path)
                path.pop()
            

            

        dfs(n, n, [])

        return res

    
                
            

        