class Solution:
    def countSubstrings(self, s: str) -> int:
        # Expand around center method

        res = 0
        n = len(s)

        for i in range(n):
            # Odd length palindrome
            l, r = i, i
            while l >=0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # Even length palindrome
            l, r, = i, i+1
            while l >=0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res

        