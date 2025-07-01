class Solution:
    def validPalindrome(self, s: str) -> bool:
        # dp = {}
        
        # def dfs(s, hasExcluded):
        #     if (s, hasExcluded) in dp:
        #         return dp[(s, hasExcluded)]
        #     if not s or s == s[::-1]:
        #         return True
            
        #     isValid = False
        #     if not hasExcluded:
        #         for i in range(len(s)):
        #             excluded_str = s[:i]+s[i+1:]
        #             if dfs(excluded_str, True):
        #                 isValid = True
        #                 break
        #     dp[(s, hasExcluded)] = isValid
        #     return dp[(s, hasExcluded)]
        
        # return dfs(s, False)

        # Greedy two pointer

        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                return s[l+1 : r+1] == s[l+1 : r+1][::-1] or s[l : r] == s[l : r][::-1]
            l += 1
            r -= 1
        return True