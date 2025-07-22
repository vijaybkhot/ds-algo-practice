class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0

        # stack = []
        # for paren in s:
        #     if paren == "(":
        #         stack.append("(")
        #     elif paren == ")":
        #         if stack:
        #             stack.pop()
        #         else:
        #             res += 1
        
        # return res + len(stack)

        left, right = 0, 0
        for paren in s:
            if paren == "(":
                left += 1
            elif paren == ")":
                if left > 0:
                    left -= 1
                else:
                    res += 1
        
        return res + left
        