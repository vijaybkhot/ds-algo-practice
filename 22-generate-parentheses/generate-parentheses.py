class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def backtrack(current, open, close):
            if len(current) == 2*n:
                result.append(current)
                return
            
            if open < n:
                backtrack(current+'(', open+1, close)
            
            if close < open:
                backtrack(current+')', open, close+1)
        
        backtrack("", 0, 0)
        return result
        
        