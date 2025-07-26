class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0

        while l < len(s) and r < len(t):
            while r < len(t) and t[r] != s[l]:
                r += 1
            if r >= len(t):
                return False
            l += 1
            r += 1
        
        if l < len(s):
            return False
        
        return True