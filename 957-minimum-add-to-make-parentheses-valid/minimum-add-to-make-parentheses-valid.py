class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0

        stack = []

       
        for paren in s:
            if paren == "(":
                stack.append("(")
            elif paren == ")":
                if stack:
                    stack.pop()
                else:
                    res += 1
        
        return res + len(stack)
        