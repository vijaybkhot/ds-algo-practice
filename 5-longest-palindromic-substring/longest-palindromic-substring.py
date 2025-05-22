class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Function to check whether a string is a palindrome
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        # # Recursion solution
        # self.longest = 0
        # self.res = None
        # def dfs(word):
        #     if len(word) <= self.longest:
        #         return

        #     if isPalindrome(word):
        #         self.longest = len(word)
        #         self.res = word
        #         return

        #     dfs(word[:-1])   
        #     dfs(word[1:])

        # dfs(s)
        # return self.res   

        # # Memoization solution - string slicing
        # self.longest = 0
        # self.res = None

        # @lru_cache(maxsize=None)
        # def dfs(word):
        #     if len(word) <= self.longest:
        #         return

        #     if isPalindrome(word):
        #         self.longest = len(word)
        #         self.res = word
        #         return
        #     if (len(word)) > self.longest:
        #         dfs(word[:-1])
        #     if (len(word)) > self.longest:
        #         dfs(word[1:])      

        # dfs(s)
        # return self.res


        # # Memoization solution - using index
        # self.longest = 0
        # self.res = None

        # @lru_cache(maxsize=None)
        # def dfs(left, right):
        #     if right - left + 1 <= self.longest:
        #         return

        #     if isPalindrome(left, right):
        #         self.longest = right - left + 1
        #         self.res = s[left:right+1]
        #         return

        #     dfs(left + 1, right)
        #     dfs(left, right - 1)

        # dfs(0, len(s) - 1)
        # return self.res

        # # Dynamic programming - bottom-up approach
        # n = len(s)
        # dp = [[False] * n for _ in range(n)]
        # start = 0
        # max_len = 1

        # for i in range(n):
        #     dp[i][i] = True  # Single characters are palindromes

        # for end in range(n):
        #     for start_idx in range(end):
        #         if s[start_idx] == s[end]:
        #             if end - start_idx == 1 or dp[start_idx + 1][end - 1]:
        #                 dp[start_idx][end] = True
        #                 if end - start_idx + 1 > max_len:
        #                     max_len = end - start_idx + 1
        #                     start = start_idx
        # return s[start:start + max_len]

        # # Expand around center:
        # res = ""
        # res_len = 0

        # for i in range(len(s)):
        #     # Odd length of palindrome
        #     l, r = i, i
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if r - l + 1 > res_len:
        #             res_len = r - l + 1
        #             res = s[l:r+1]
        #         l -= 1
        #         r += 1
            
        #     # Even length of palidrome
        #     l, r = i, i+1
        #     while l >= 0 and r < len(s) and  s[l] == s[r]:
        #         if r - l + 1 > res_len:
        #             res_len = r - l + 1
        #             res = s[l:r+1]
        #         l -= 1
        #         r += 1
        
        # return res

        # Bottom-up dynamic programming
        n = len(s)
        dp = [[0]*n for i in range(n)]
        res = ""
        max_len = 0

        n = len(s)
        dp = [[0]*n for i in range(n)]
        res = ""
        max_len = 0

        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = 1
            max_len = 1
            res = s[i]

        # Check substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                max_len = 2
                res = s[i:i + 2]

        for i in range(2, n):
            for left in range(n-i):
                right = left + i
                if s[left] == s[right] and dp[left+1][right-1] == 1:
                    dp[left][right] = 1
                    if max_len < right-left+1:
                        max_len = right-left+1
                        res = s[left:right+1]

                
        
        return res
            

