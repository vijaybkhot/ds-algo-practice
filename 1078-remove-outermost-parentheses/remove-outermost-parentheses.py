class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        left, right = 0, 0
        start = 0
        for idx, paren in enumerate(s):
            if paren == "(":
                left += 1
            elif paren == ")":
                right += 1
            if left == right:
                res += s[start+1:idx]
                start = idx + 1
        
        return res

