class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0

        # Left to right pass
        left, right = 0, 0
        for idx, paren in enumerate(s):
            if paren == "(":
                left += 1
            elif paren == ")":
                right += 1
                if left == right:
                    res = max(res, 2 * right)
                elif right > left:
                    left = right = 0


        # Right to left pass
        left, right = 0, 0
        for idx in range(len(s)-1, -1, -1):
            paren = s[idx]
            if paren == "(":
                left += 1
                if left == right:
                    res = max(res, 2 * left)
                elif left > right:
                    left = right = 0
            elif paren == ")":
                right += 1
                

        return res