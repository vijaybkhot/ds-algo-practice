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

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1

        for i in range(n):
            dp[i][i] = True  # Single characters are palindromes

        for end in range(n):
            for start_idx in range(end):
                if s[start_idx] == s[end]:
                    if end - start_idx == 1 or dp[start_idx + 1][end - 1]:
                        dp[start_idx][end] = True
                        if end - start_idx + 1 > max_len:
                            max_len = end - start_idx + 1
                            start = start_idx
        return s[start:start + max_len]