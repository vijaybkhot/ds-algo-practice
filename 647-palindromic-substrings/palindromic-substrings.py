class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)

        # # Expand around center method
        # res = 0
        # for i in range(n):
        #     # Odd length palindrome
        #     l, r = i, i
        #     while l >=0 and r < n and s[l] == s[r]:
        #         res += 1
        #         l -= 1
        #         r += 1
        #     # Even length palindrome
        #     l, r, = i, i+1
        #     while l >=0 and r < n and s[l] == s[r]:
        #         res += 1
        #         l -= 1
        #         r += 1
        # return res

        # Bottom-up dynamic programming approach
        res = 0
        dp = [[0]*n for _ in range(n)]
        
        # Palindromes of length 1
        for i in range(n):
            dp[i][i] = 1
            res += 1
        
        # Palindromes of length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                res += 1
        
        # Main dp logic for palindroms of length 3 and onwards
        for i in range(2, n):
            for left in range(n-i):
                right = left + i
                if s[left] == s[right] and dp[left+1][right-1] == 1:
                    dp[left][right] = 1
                    res += 1
        
        return res



        