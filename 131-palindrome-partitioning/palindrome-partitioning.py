class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # def isPalindrome(word):
        #     # return word == word[::-1]
        #     left, right = 0, len(word)-1
        #     while left <= right:
        #         if word[left] != word[right]:
        #             return False
        #         left += 1
        #         right -= 1
        #     return True
        
        # res = []
        # def backtrack(start, path):
        #     if start == len(s):
        #         res.append(path[:])
        #         return
            
        #     for i in range(start, len(s)):
        #         if isPalindrome(s[start:i+1]):
        #             path.append(s[start:i+1])
        #             backtrack(i+1, path)
        #             path.pop()

        # backtrack(0, [])
        # return res


        def is_palindrome(word):
            return word == word[::-1]
        
        res = []
        def dfs(start, path):
            if start == len(s):
                res.append(path[:])
                return
            
            for i in range(start, len(s)):
                left = s[start:i+1]
                right = s[i+1:]
                if is_palindrome(left):
                    path.append(left)
                    dfs(i+1, path)
                    path.pop()
        dfs(0, [])
        return res
            
