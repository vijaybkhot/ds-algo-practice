class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        self.res= []
        # def dfs(i, j, path):
        #     if i == 0 and j == 0:
        #         self.res.append(path)
        #         return
            
        #     if i > 0 and i >= j:
        #         dfs(i-1, j, path+"(")
        
        #     else:
        #         if i > 0:
        #             dfs(i-1, j, path+"(")
        #         if j > 0:
        #             dfs(i, j-1, path+")")
        

        def dfs(i, j, path):
            if i == 0 and j == 0:
                self.res.append(path)
                return
            
            if i > 0:
                dfs(i-1, j, path+"(")
            if j > i:
                dfs(i, j-1, path+")")


        dfs(n, n, "")
        return self.res
















        # res = []

        # def dfs(open_paren, closed_paren, path):
        #     if len(path) == 2*n:
                
        #         res.append(''.join(path[:]))
        #         return
        

        #     if open_paren == n:
        #         path.append('(')
        #         dfs(open_paren-1, closed_paren, path)
        #         path.pop()
            
        #     elif open_paren == 0:
        #         path.append(')')
        #         dfs(open_paren, closed_paren-1, path)
        #         path.pop()

        #     elif (open_paren <= closed_paren) and (open_paren > 0):
        #         path.append('(')
        #         dfs(open_paren-1, closed_paren, path)
        #         path.pop()

        #         path.append(')')
        #         dfs(open_paren, closed_paren-1, path)
        #         path.pop()
            

            

        # dfs(n, n, [])

        # return res

    
                
            

        